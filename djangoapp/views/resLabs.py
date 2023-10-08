from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..permissions import Cadastrado
from ..models import ResLab
from ..serializers import ResLabSerializer
from utils.funcs_gerais import gerar_code_pay,byte_to_dict
from utils.api_requests import requisicao_api


@api_view(["GET"])
@permission_classes([Cadastrado])
def getData(request):
    resLab = ResLab.objects.all()
    serializer = ResLabSerializer(resLab, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([Cadastrado])
def getResLab(request, pk):
    resLab = ResLab.objects.get(id=pk)
    serializer = ResLabSerializer(resLab, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([Cadastrado])
def addResLab(request):
    serializer = ResLabSerializer(data=request.data)
    if serializer.is_valid():
        code_pay = gerar_code_pay()
        url = 'https://api-go-wash-efc9c9582687.herokuapp.com/api/pay-boleto'
        headers = {
            # Substitua pelo token JWT adequado
            'Authorization': 'Vf9WSyYqnwxXODjiExToZCT9ByWb3FVsjr',
            'Content-Type': 'application/json',
            'Cookie': 'gowash_session=m6Y5t4HwextNyZIPR4uCOD97ebOoYusUfmRMwt06',
        }
        body = {
            "boleto": code_pay,
            "user_id": request.data["user_id"]
        }
        content = byte_to_dict(requisicao_api(url, headers, body)._content)
        print(content)
        if 'data' in content and content['data']['status'] == 'approved':
            serializer.save()
        elif 'errors' in content:
            return Response({
                        "mensagem": content["errors"]["boleto"][0]
                    })
        else:
            return Response({
                        "mensagem": "Não foi possível fazer a reserva, por favor tentar mais tarde."
                    })
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([Cadastrado])
def updateResLab(request, pk):
    lab = ResLab.objects.get(id=pk)
    serializer = ResLabSerializer(instance=lab, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([Cadastrado])
def deleteResLab(request, pk):
    lab = ResLab.objects.get(id=pk)
    lab.delete()
    return Response("ResLab deletado com sucesso!")
