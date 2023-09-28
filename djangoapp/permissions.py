from rest_framework import permissions
from .models import User

class Professor(permissions.BasePermission):
    def has_permission(self, request, view):
        # request.user = User.objects.get(id=payload["user_id"])
        # if request.user:
        #     # Verificar se o user_type_id é igual a 1
        #     return True
        return False  # Se o usuário não estiver autenticado ou o user_type_id não for 1, nega permissão
