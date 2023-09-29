from rest_framework import permissions
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings

def decode_token(token):
    try:
        # A chave secreta usada para assinar o token JWT
        secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
        
        # Decodifica o token
        algorithm = settings.SIMPLE_JWT["ALGORITHM"]
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        print(f'PAYLOD: {payload}')
        
        # O 'payload' agora contém as informações do token decodificado
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token expirado. Faça login novamente.')
    except jwt.DecodeError:
        raise AuthenticationFailed('Token inválido. Faça login novamente.')
    
class Professor(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split("Bearer ")[1]
        token = token.replace('"', '')
        print(f'TOKEN: {token}')
        payload = decode_token(token)
        request.user = User.objects.get(id=request.user["user_id"])
        if request.user:
            # Verificar se o user_type_id é igual a 1
            return True
        return False  # Se o usuário não estiver autenticado ou o user_type_id não for 1, nega permissão
