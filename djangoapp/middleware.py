import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.conf import settings
from .models import User

def decode_token(token):
    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None

def get_token(header):
    token = header.split("Bearer ")[1]
    token = token.replace('"', "")
    return token

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.META.get("HTTP_AUTHORIZATION")
        if authorization_header:
            token = get_token(authorization_header)
            if token:
                payload = decode_token(token)
                if payload:
                    request.auth_payload = payload
                    request.user = User.objects.get(id=payload["user_id"])
                else:
                    error_message = "Token invalido ou expirado."
                    return JsonResponse({"error": error_message}, status=401)

        response = self.get_response(request)
        return response
