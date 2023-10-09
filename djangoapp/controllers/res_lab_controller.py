from rest_framework.response import Response
from ..models import Res_Lab
from ..serializers import Res_Lab_Serializer
from utils.funcs_gerais import gerar_code_pay,byte_to_dict
from utils.api_requests import requisicao_api

def get_all_res_lab(request):
    res_lab = Res_Lab.objects.all()
    serializer = Res_Lab_Serializer(res_lab, many=True)
    return Response(serializer.data)


def get_res_lab(request, pk):
    res_lab = Res_Lab.objects.get(id=pk)
    serializer = Res_Lab_Serializer(res_lab, many=False)
    return Response(serializer.data)



def add_res_Lab(request):
    serializer = Res_Lab_Serializer(data=request.data)
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



def update_res_lab(request, pk):
    lab = Res_Lab.objects.get(id=pk)
    serializer = Res_Lab_Serializer(instance=lab, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



def delete_res_lab(request, pk):
    lab = Res_Lab.objects.get(id=pk)
    lab.delete()
    return Response("Res_Lab deletado com sucesso!")
