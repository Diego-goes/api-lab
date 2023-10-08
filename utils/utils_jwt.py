import jwt
from django.conf import settings
from datetime import datetime, timedelta


def decode_token(token):
    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None


def get_token(header):
    token = header.split("Bearer ")[1]
    token = token.replace('"', "")
    return token


def gera_token(user):
    exp_timestamp = datetime.now() + timedelta(days=7)
    # Defina as informações que deseja incluir no payload (carga útil) do JWT
    payload = {
        'user_id': user.id,
        'username': user.name,
        'user_type_id': user.user_type_id,
        'exp': exp_timestamp
        # Outras informações personalizadas podem ser adicionadas aqui
    }

    # Acesse a chave secreta e o algoritmo diretamente de settings
    secret_key = settings.SIMPLE_JWT["SIGNING_KEY"]
    # Supondo que você tenha definido JWT_ALGORITHM em settings.py
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]

    # Gere o token JWT
    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    # Retorna o token como uma resposta JSON
    return token
