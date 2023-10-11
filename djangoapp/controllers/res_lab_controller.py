from rest_framework.response import Response
from ..models import Res_Lab
from ..serializers import Res_Lab_Serializer
from utils.funcs_gerais import gerar_code_pay, byte_to_dict
from utils.api_requests import requisicao_api
from rest_framework import status


def confirmar_pagamento(code_pay, user_id):
    # Tenta realizar o pagamento consumindo a API, caso 'approved', retorna True, ao contrario retorna mensagem de erro.
    url = 'https://api-go-wash-efc9c9582687.herokuapp.com/api/pay-boleto'
    headers = {
        # Credenciais para usar a API
        'Authorization': 'Vf9WSyYqnwxXODjiExToZCT9ByWb3FVsjr',
        'Content-Type': 'application/json',
        'Cookie': 'gowash_session=m6Y5t4HwextNyZIPR4uCOD97ebOoYusUfmRMwt06',
    }
    body = {
        "boleto": code_pay,
        "user_id": user_id
    }
    content = byte_to_dict(requisicao_api(url, headers, body)._content)
    if 'data' in content and content['data']['status'] == 'approved':
        return True
    elif 'errors' in content:
        return {"mensagem": content["errors"]["boleto"][0]}
    else:
        return {"mensagem": "Não foi possível fazer a reserva, por favor tentar mais tarde."}
def validar_reserva(res_date):
    return not Res_Lab.objects.filter(res_date=res_date).exists()

def validar_horario(res_date):
    horario = res_date.split("T")[1]
    horario = horario.split(":")
    m = int(horario[1])
    s = int(horario[2].replace("Z",""))
    return m == 0 and s == 0

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
    if not serializer.is_valid():
        # Handle invalid serializer data
        response_data = {
            'Mensagem': 'Não foi possível concluir a ação, existem dados inválidos.',
            'body': f'{serializer.data}',
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    dados = request.data
    res_date = dados['res_date']

    if not validar_horario(res_date):
        return Response({'Mensagem': 'Não foi possível concluir a ação, o horário não é válido.'}, status=status.HTTP_400_BAD_REQUEST)

    if not validar_reserva(res_date):
        return Response({'Mensagem': 'Não foi possível concluir a ação, o horário não está mais disponível para essa data.'}, status=status.HTTP_400_BAD_REQUEST)

    code_pay = gerar_code_pay()
    status_pay = confirmar_pagamento(code_pay, dados["user_id"])

    if status_pay:
        serializer.save()
        return Response('Pagamento confirmado, reserva efetuada.')
    else:
        return Response(status_pay, status=status.HTTP_400_BAD_REQUEST)


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
