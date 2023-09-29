from rest_framework import permissions
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings

def decode_token(token):
    # try:
        # A chave secreta usada para assinar o token JWT
        secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
        
        # Decodifica o token
        algorithm = settings.SIMPLE_JWT["ALGORITHM"]
        # Teste
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozNSwidXNlcm5hbWUiOiJQcm9mZXNzb3IiLCJ1c2VyX3R5cGVfaWQiOjEsImV4cCI6MTY5NTY4NjQwMH0.mdxFtNeF7jvDfIyeYi4LVl-BIivG4w0P339y7k8RwDs"
        # secret_key = "cfh58$*%jf*%584mf*4jJf8J*&fh789J*H)$#-3JFej()(#_)mf#*(593)"
        # algorithm = "HS256"

        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        print(f'PAYLOD: {payload}')
        
        # O 'payload' agora contém as informações do token decodificado
        return payload
    
class Professor(permissions.BasePermission):
    def has_permission(self, request, view):
        authorization_header  = request.META.get("HTTP_AUTHORIZATION")
        if authorization_header:
            token = request.META.get("HTTP_AUTHORIZATION").split("Bearer ")[1]
            token = token.replace('"', '')
            print(f'TOKEN: {token}')
            payload = decode_token(token)
            request.user = User.objects.get(id=payload["user_id"])
            if request.user:
                # Verificar se o user_type_id é igual a 1
                return True
        return False  # Se o usuário não estiver autenticado ou o user_type_id não for 1, nega permissão
