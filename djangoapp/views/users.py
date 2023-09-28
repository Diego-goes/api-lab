from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import User
from ..serializers import UserSerializer

@api_view(["GET"])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

@api_view(["POST"])
def inativarUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active == 1:
            user.is_active = 0
            user.save()
            return Response({f"User inativado com sucesso!"})
        else:
            return Response({f"User ja estava inativado!"})
    except User.DoesNotExist:
        return Response({"User não encontrado"})


@api_view(["POST"])
def ativarUser(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.is_active == 0:
            user.is_active = 1
            user.save()
            return Response({f"User ativado com sucesso!"})
        else:
            return Response({f"User ja estava ativado!"})
    except User.DoesNotExist:
        return Response({"User não encontrado"})


@api_view(["PUT"])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response("User successfully deleted!")
