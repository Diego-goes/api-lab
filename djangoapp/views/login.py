from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import User


@api_view(["POST"])
def login(request):
    dados = request.data

    # Verifica se os campos "email" e "password" existem no JSON
    if "email" in dados and "password" in dados:
        email = dados["email"]
        password = dados["password"]

        try:
            # Tenta encontrar um usuário com o email fornecido
            usuario = User.objects.get(email=email)

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
        return Response({"mensagem": 'Campos "email" e "password" são obrigatórios'})
