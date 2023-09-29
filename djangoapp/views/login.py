from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from ..models import User
from django.conf import settings
<<<<<<< HEAD
from datetime import datetime
=======
from datetime import datetime, timedelta
>>>>>>> 664b05a (Tentativa promissora)


# from rest_framework_simplejwt.tokens import RefreshToken
import jwt


def gera_token(user):
<<<<<<< HEAD
    data_expiracao = datetime(2023, 9, 26)
    exp_timestamp = int(data_expiracao.timestamp())
=======
    exp_timestamp = datetime.now() + timedelta(days=7)
>>>>>>> 664b05a (Tentativa promissora)
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
    algorithm = settings.SIMPLE_JWT["ALGORITHM"]  # Supondo que você tenha definido JWT_ALGORITHM em settings.py

    # Gere o token JWT
    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    # Retorna o token como uma resposta JSON
    return token



@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    dados = request.data

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
                access_token = gera_token(usuario)

                return Response(
                    {
                        "mensagem": "Login bem-sucedido",
                        "usuario_id": usuario.id,
                        "access_token": access_token,
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
<<<<<<< HEAD
        )
=======
        )
>>>>>>> 664b05a (Tentativa promissora)
