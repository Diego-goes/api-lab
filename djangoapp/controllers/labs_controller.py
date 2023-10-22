from rest_framework.response import Response
from ..models import Lab
from ..serializers import Lab_Serializer
from rest_framework import status


def get_all_labs(request):
    labs = Lab.objects.all()
    serializer = Lab_Serializer(labs, many=True)
    return Response(serializer.data)



def get_lab(request, pk):
    try:
        labs = Lab.objects.get(id=pk)
        serializer = Lab_Serializer(labs, many=False)
        return Response(serializer.data)
    except Lab.DoesNotExist:
        return Response({f"Laboratório {pk} não encontrado"})



def add_lab(request):
    dados = request.data
    if "andar" in dados and "lab" in dados:
        andar = dados["andar"]

        if Lab.objects.filter(andar=andar).exists():
            return Response({f"Já existe um laboratório registrado no andar {andar}, escolha um outro andar."})

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
            return Response({f"Laboratório {pk} inativado com sucesso!"})
        else:
            return Response({f"Laboratório {pk} ja estava inativado!"})
    except Lab.DoesNotExist:
        return Response({f"Laboratório {pk} não encontrado"})



def ativar_lab(request, pk):
    try:
        lab = Lab.objects.get(id=pk)
        if lab.is_active == 0:
            lab.is_active = 1
            lab.save()
            return Response({f"Laboratório {pk} ativado com sucesso!"})
        else:
            return Response({f"Laboratório {pk} ja estava ativado!"})
    except Lab.DoesNotExist:
        return Response({f"Laboratório {pk} não encontrado"})



def update_lab(request, pk):    
    try:
        lab = Lab.objects.get(id=pk)
        serializer = Lab_Serializer(instance=lab, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'Mensagem': f'Laboratório {pk} atualizado com sucesso!', 'body': serializer.data}, status=status.HTTP_202_ACCEPTED)
    except Lab.DoesNotExist:
        return Response({f"Laboratório {pk} não encontrado"})




def delete_lab(request, pk):
    try:
        lab = Lab.objects.get(id=pk)
        lab.delete()
        return Response(f"Laboratório {pk} deletado com sucesso!")
    except Lab.DoesNotExist:
        return Response({f"Laboratório {pk} não encontrado"})
