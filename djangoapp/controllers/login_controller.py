from rest_framework.response import Response
from rest_framework import status
from ..models import User
from utils.utils_jwt import gera_token

def login_user(dados):
    if "cpf_cnpj" in dados and "password" in dados:
        cpf_cnpj = dados["cpf_cnpj"]
        password = dados["password"]

        try:
            # Tenta encontrar um usuário com o cpf_cnpj fornecido
            usuario = User.objects.get(cpf_cnpj=cpf_cnpj)

            if usuario.is_active == 0:
                return Response(
                    {
                        "mensagem": "Não foi possível realizar o login, pois o usuário está inativo."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            # Verifica se a senha fornecida corresponde à senha armazenada no banco de dados
            if password == usuario.password:
                # Senha correta, você pode fazer algo com o usuário agora

                # Cria um token JWT
                token_jwt = gera_token(usuario)

                return Response(
                    {
                        "mensagem": "Login bem-sucedido",
                        "usuario_id": usuario.id,
                        "token_jwt": token_jwt,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"mensagem": "Senha incorreta"}, status=status.HTTP_401_UNAUTHORIZED
                )
        except User.DoesNotExist:
            return Response(
                {"mensagem": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
    else:
        return Response(
            {"mensagem": "Campos 'cpf_cnpj' e 'password' são obrigatórios"},
            status=status.HTTP_400_BAD_REQUEST,
        )
