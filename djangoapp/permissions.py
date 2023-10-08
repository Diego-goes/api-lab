from rest_framework import permissions

class Professor(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("user_type_id") == 1:
                return True
        return False

class Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            if payload.get("user_type_id") == 0:
                return True
        return False

class PodeEditarPerfil(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            payload = request.auth_payload
            user_id = payload.get("user_id")
            user_type_id = payload.get("user_type_id")
            url_pk = int(view.kwargs.get('pk'))  # Obtém a PK da URL
            if user_id == url_pk or user_type_id == 0:
                return True
        return False
class Cadastrado(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
            return True
        return False

class IsProfessorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request, 'auth_payload') and request.auth_payload:
        # Verifica se o usuário é um professor ou um admin master
            payload = request.auth_payload
            user_type_id = payload.get("user_type_id")
            if user_type_id == 0 or user_type_id == 1:
                return True
        return False
