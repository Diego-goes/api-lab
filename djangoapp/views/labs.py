from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Lab
from ..serializers import LabSerializer


@api_view(["GET"])
def getData(request):
    labs = Lab.objects.all()
    serializer = LabSerializer(labs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getLab(request, pk):
    labs = Lab.objects.get(id=pk)
    serializer = LabSerializer(labs, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addLab(request):
    serializer = LabSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def updateLab(request, pk):
    lab = Lab.objects.get(id=pk)
    serializer = LabSerializer(instance=lab, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteLab(request, pk):
    lab = Lab.objects.get(id=pk)
    lab.delete()
    return Response("Lab successfully deleted!")
