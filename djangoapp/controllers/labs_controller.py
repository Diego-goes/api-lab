from rest_framework.response import Response
from ..models import Lab
from ..serializers import Lab_Serializer


def get_all_labs(request):
    labs = Lab.objects.all()
    serializer = Lab_Serializer(labs, many=True)
    return Response(serializer.data)



def get_lab(request, pk):
    labs = Lab.objects.get(id=pk)
    serializer = Lab_Serializer(labs, many=False)
    return Response(serializer.data)



def add_lab(request):
    dados = request.data
    if "andar" in dados and "lab" in dados:
        andar = dados["andar"]
        lab = dados["lab"]

        try:
            if Lab.objects.filter(andar=andar).exists():
                return Response({f"O Lab tem já está registrado no andar {andar}."})
            
        except Lab.DoesNotExist:
            return Response({"Laboratório não encontrado."})

        serializer = Lab_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response({"mensagem": "Existem campos faltando."})


def inativar_lab(request, pk):
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



def ativar_lab(request, pk):
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



def update_lab(request, pk):
    lab = Lab.objects.get(id=pk)
    serializer = Lab_Serializer(instance=lab, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



def delete_lab(request, pk):
    lab = Lab.objects.get(id=pk)
    lab.delete()
    return Response("Lab successfully deleted!")