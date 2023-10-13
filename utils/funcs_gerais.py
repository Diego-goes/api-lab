from random import randint
import json
from .api_requests import requisicao_api
def gerar_code_pay():
    code_pay = str(randint(0,99999999))
    if len(code_pay) != 8:
        casas_decimais_ausentes = 8 - len(code_pay)
        code_pay = casas_decimais_ausentes*"0" + code_pay
    return code_pay

def byte_to_dict(data):
    data_string = data.decode('utf-8')
    dictionary = json.loads(data_string)
    return dictionary

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
