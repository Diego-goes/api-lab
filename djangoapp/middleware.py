import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.conf import settings
from .models import User
from utils.utils_jwt import decode_token, get_token


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.META.get("HTTP_AUTHORIZATION")
        if authorization_header:
            token = get_token(authorization_header)
            if token:
                payload = decode_token(token)
                try:
                    request.auth_payload = payload
                    request.user = User.objects.get(id=payload["user_id"])
                except:
                    error_message = "Token invalido ou expirado."
                    return JsonResponse({"error": error_message}, status=401)

        response = self.get_response(request)
        return response
