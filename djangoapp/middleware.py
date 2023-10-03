import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from .models import User


def decode_token(token):
    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]
    payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    return payload

def get_token(header):
    token = header.split("Bearer ")[1]
    token = token.replace('"', "")  
    return token

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtenha o token do cabeçalho da solicitação
        authorization_header = request.META.get("HTTP_AUTHORIZATION")
        if authorization_header:
            token = get_token(authorization_header)
            if token:
                try:
                    payload = decode_token(token)
                    # Defina o usuário autenticado no objeto de solicitação
                    request.auth_payload = payload
                    request.user = User.objects.get(id=payload["user_id"])
                    # print(request.__dict__)
                except jwt.ExpiredSignatureError:
                    return AuthenticationFailed("Token expirado. Faça login novamente.")
                except jwt.DecodeError:
                    return AuthenticationFailed("Token inválido. Faça login novamente.")

        response = self.get_response(request)
        return response
