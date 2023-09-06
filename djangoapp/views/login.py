from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import User


@api_view(["POST"])
def login(request):
    dados = request.data

    if "cpf_cnpj" in dados and "password" in dados:
        cpf_cnpj = dados["cpf_cnpj"]
        password = dados["password"]

        try:
            # Tenta encontrar um usuário com o email fornecido
            usuario = User.objects.get(cpf_cnpj=cpf_cnpj)

            if usuario.is_active == 0:
                return Response(
                    {"Não foi possível realizar o login, pois o usuário está inativo."}
                )
            # Verifica se a senha fornecida corresponde à senha armazenada no banco de dados
            if password == usuario.password:
                # Senha correta, você pode fazer algo com o usuário agora
                return Response(
                    {"mensagem": "Login bem-sucedido", "usuario_id": usuario.id}
                )
            else:

                return Response({"mensagem": "Senha incorreta"})

        except User.DoesNotExist:
            return Response({"mensagem": "Usuário não encontrado"})
    else:
        return Response({"mensagem": 'Campos "cpf_cnpj" e "password" são obrigatórios'})
