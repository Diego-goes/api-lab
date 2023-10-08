from random import randint
import json

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