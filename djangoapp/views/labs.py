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
    dados = request.data
    if "andar" in dados and "lab" in dados:
        andar = dados["andar"]
        lab = dados["lab"]

        try:
            if Lab.objects.filter(andar=andar).exists():
                return Response({f"O Lab tem já está registrado no andar {andar}."})
            
        except Lab.DoesNotExist:
            return Response({"Laboratório não encontrado."})

        serializer = LabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response({"mensagem": "Existem campos faltando."})

@api_view(["POST"])
def inativarLab(request, pk):
    try:
        lab = Lab.objects.get(id=pk)
        if lab.is_active == 1:
            lab.is_active = 0
            lab.save()
            return Response({f"Lab inativado com sucesso!"})
        else:
            return Response({f"Lab ja estava inativado!"})
    except Lab.DoesNotExist:
        return Response({"Laboratório não encontrado"})


@api_view(["POST"])
def ativarLab(request, pk):
    try:
        lab = Lab.objects.get(id=pk)
        if lab.is_active == 0:
            lab.is_active = 1
            lab.save()
            return Response({"Lab ativado com sucesso!"})
        else:
            return Response({"Lab ja estava ativado!"})
    except Lab.DoesNotExist:
        return Response({"Laboratório não encontrado"})


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
