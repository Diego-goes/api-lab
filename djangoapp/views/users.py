from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..permissions import Professor, Admin, PodeEditarPerfil,Cadastrado,IsProfessorOrAdmin
from rest_framework.permissions import AllowAny
from ..models import User
from ..serializers import UserSerializer

@api_view(["GET"])
@permission_classes([IsProfessorOrAdmin])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([PodeEditarPerfil])
def getUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"message": "User não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404

@api_view(["POST"])
@permission_classes([AllowAny])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@permission_classes([PodeEditarPerfil])
def inativarUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active == 1:
            user.is_active = 0
            user.save()
            return Response({"message": "User inativado com sucesso!"})
        else:
            return Response({"message": "User já estava inativado!"})
    except User.DoesNotExist:
        return Response({"message": "User não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404

@api_view(["POST"])
@permission_classes([Admin])
def ativarUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active == 0:
            user.is_active = 1
            user.save()
            return Response({"message": "User ativado com sucesso!"})
        else:
            return Response({"message": "User já estava ativado!"})
    except User.DoesNotExist:
        return Response({"message": "User não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404

@api_view(["PUT"])
@permission_classes([PodeEditarPerfil])
def updateUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"message": "User não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404

@api_view(["DELETE"])
@permission_classes([Admin])
def deleteUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response("User successfully deleted!")
    except User.DoesNotExist:
        return Response({"message": "User não encontrado"}, status=404)  # Retorna uma resposta de erro com status 404
