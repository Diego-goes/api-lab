import requests

def requisicao_api(url, headers, body):

    try:
        response = requests.post(url, json=body, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        # Trate qualquer erro de requisição aqui
        print(f"Erro na requisição: {e}")
        return {"message": f"Erro ao enviar a requisição: {e}"}
