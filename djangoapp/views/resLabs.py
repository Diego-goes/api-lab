from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..permissions import Professor 
from rest_framework.permissions import AllowAny
from ..models import ResLab
from ..serializers import ResLabSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def getData(request):
    resLab = ResLab.objects.all()
    serializer = ResLabSerializer(resLab, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def getResLab(request, pk):
    resLab = ResLab.objects.get(id=pk)
    serializer = ResLabSerializer(resLab, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def addResLab(request):
    serializer = ResLabSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([AllowAny])
def updateResLab(request, pk):
    lab = ResLab.objects.get(id=pk)
    serializer = ResLabSerializer(instance=lab, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([AllowAny])
def deleteResLab(request, pk):
    lab = ResLab.objects.get(id=pk)
    lab.delete()
    return Response("ResLab successfully deleted!")
