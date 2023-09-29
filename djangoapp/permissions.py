from rest_framework import permissions


class Professor(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.__dict__["_full_data"])
        payload = request.auth_payload
        if payload and payload["user_type_id"] == 1:
            # print(request.auth_payload)
            return True
