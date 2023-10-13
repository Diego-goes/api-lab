from rest_framework.response import Response
from ..models import Res_Lab
from ..serializers import Res_Lab_Serializer
from utils.funcs_gerais import gerar_code_pay, confirmar_pagamento
from utils.funcs_bd import lab_existe, user_existe
from rest_framework import status
from datetime import datetime, timedelta


def horario_expirado(res_date):
    data_atual = datetime.now()
    res_date = res_date.replace('Z', '')
    res_date = datetime.fromisoformat(res_date)
    return not res_date > data_atual


def reserva_valida(res_date):
    return not Res_Lab.objects.filter(res_date=res_date).exists()


def horario_valido(res_date):
    horario = res_date.split("T")[1]
    horario = horario.split(":")
    m = int(horario[1])
    s = int(horario[2].replace("Z", ""))
    return m == 0 and s == 0


def validacoes_gerais_hr(res_date):
    if horario_expirado(res_date):
        return Response({'Mensagem': 'Não foi possível concluir a ação, o horario já se passou.'}, status=status.HTTP_400_BAD_REQUEST)
    if not horario_valido(res_date):
        return Response({'Mensagem': 'Não foi possível concluir a ação, o horário não é válido.'}, status=status.HTTP_400_BAD_REQUEST)
    if not reserva_valida(res_date):
        return Response({'Mensagem': 'Não foi possível concluir a ação, o horário não está mais disponível para essa data.'}, status=status.HTTP_400_BAD_REQUEST)


def get_all_res_lab(request):
    res_lab = Res_Lab.objects.all()
    serializer = Res_Lab_Serializer(res_lab, many=True)
    return Response(serializer.data)


def get_res_lab(request, pk):
    try:
        res_lab = Res_Lab.objects.get(id=pk)
        serializer = Res_Lab_Serializer(res_lab, many=False)
        return Response(serializer.data)
    except Res_Lab.DoesNotExist:
        return Response({"message":f"Não foi possível concluir a ação, reserva {pk} não encontrada."})


def add_res_Lab(request):
    serializer = Res_Lab_Serializer(data=request.data)
    
    if not serializer.is_valid():
        response_data = {
            'Mensagem': 'Não foi possível concluir a ação, existem dados inválidos.',
            'body': f'{serializer.data}',
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    if 'res_date' not in request.data:
        return Response({
            'Mensagem': 'Não foi possível concluir a ação, horário da reserva ausente.',
            'body': f'{serializer.data}',
        })
    res_date = request.data['res_date']
    response = validacoes_gerais_hr(res_date)

    if response:
        return response

    code_pay = gerar_code_pay()
    status_pay = confirmar_pagamento(code_pay, request.data["user_id"])

    if status_pay:
        serializer.save()
        return Response({'message':'Pagamento confirmado, reserva efetuada.'})
    else:
        return Response(status_pay, status=status.HTTP_400_BAD_REQUEST)



def update_res_lab(request, pk):
    dados = request.data
    try:
        res_lab = Res_Lab.objects.get(id=pk)
    except Res_Lab.DoesNotExist:
        return Response({"message":f"Não foi possível concluir a ação, reserva {pk} não encontrada."})
    try:
        user_response = user_existe(dados["user_id"])
        lab_response = lab_existe(dados["lab_id"])
        date_response = validacoes_gerais_hr(dados["res_date"])
    except:
        return Response({"mensagem": "Não foi possível concluir a ação, existem campos faltando."})


    if user_response or lab_response or date_response:
        return user_response or lab_response or date_response

    serializer = Res_Lab_Serializer(instance=res_lab, data=dados)

    if serializer.is_valid():
        serializer.save()
        return Response({"mensagem": f"Reserva {pk} atualizada com sucesso.", f"reserva{pk}": serializer.data})
    else:
        return Response({"mensagem": "Não foi possível concluir a ação, existem campos faltando."})



def delete_res_lab(request, pk):
    try:
        res_lab = Res_Lab.objects.get(id=pk)
    except Res_Lab.DoesNotExist:
        return Response({"message": f"Não foi possível concluir ação, pois a reserva {id} não existe."})

    res_lab.delete()
    return Response({'message':'Res_Lab deletado com sucesso!'})
