from rest_framework.decorators import api_view, permission_classes
from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..controllers import users_controller

@api_view(["GET"])
@permission_classes([IsProfessorOrAdmin])
def get_all_users_view(request):
   return users_controller.get_all_users(request)

@api_view(["GET"])
@permission_classes([PodeEditarPerfil])
def get_user_view(request, pk):
   return users_controller.get_user(request,pk)

@api_view(["POST"])
@permission_classes([AllowAny])
def add_user_view(request):
   return users_controller.add_user(request)

@api_view(["POST"])
@permission_classes([PodeEditarPerfil])
def inativar_user_view(request, pk):
   return users_controller.inativar_user(request,pk)

@api_view(["POST"])
@permission_classes([Admin])
def ativar_user_view(request, pk):
   return users_controller.ativar_user(request,pk)

@api_view(["PUT"])
@permission_classes([PodeEditarPerfil])
def update_user_view(request, pk):
   return users_controller.update_user(request,pk)

@api_view(["DELETE"])
@permission_classes([Admin])
def delete_user_view(request, pk):
   return users_controller.delete_user(request,pk)
