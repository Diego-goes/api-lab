from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import User
from ..serializers import User_Serializer


def get_all_users(request):
    users = User.objects.all()
    serializer = User_Serializer(users, many=True)
    return Response(serializer.data)


def get_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = User_Serializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def add_user(request):
    serializer = User_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Usuário criado com sucesso!"}, status=200)
    else:
        return Response({"message": "Não foi possível criar o usuário, revise os campos e tente novamente!"}, status=404)


def inativar_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active == 1:
            user.is_active = 0
            user.save()
            return Response({"message": "Usuário inativado com sucesso!"})
        else:
            return Response({"message": "Usuário já estava inativado!"})
    except User.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def ativar_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active == 0:
            user.is_active = 1
            user.save()
            return Response({"message": "Usuário ativado com sucesso!"})
        else:
            return Response({"message": "Usuário já estava ativado!"})
    except User.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def update_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = User_Serializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404


def delete_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response("Usuário successfully deleted!")
    except User.DoesNotExist:
        return Response({"message": "Usuário não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404
