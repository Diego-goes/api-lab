import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from .models import User

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtenha o token do cabeçalho da solicitação
        authorization_header  = request.META.get("HTTP_AUTHORIZATION")
        if authorization_header:
            token = authorization_header .split("Bearer ")[1]
            token = token.replace('"', '')
            if token:
                try:
                    # A chave secreta usada para assinar o token JWT
                    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
                    
                    # Decodifica o token
                    algorithm = settings.SIMPLE_JWT["ALGORITHM"]
                    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
                    # Defina o usuário autenticado no objeto de solicitação
                    request.paylod = payload
                    request.user = User.objects.get(id=payload["user_id"])
                    # print(request.__dict__)
                except jwt.ExpiredSignatureError:
                    return AuthenticationFailed('Token expirado. Faça login novamente.')
                except jwt.DecodeError:
                    return AuthenticationFailed('Token inválido. Faça login novamente.')

        response = self.get_response(request)
<<<<<<< HEAD
        return response
=======
        return response
>>>>>>> 664b05a (Tentativa promissora)
