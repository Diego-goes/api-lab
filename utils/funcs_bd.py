from djangoapp.models import Res_Lab, User, Lab
from rest_framework.response import Response


def user_existe(id):
    if not User.objects.filter(id=id).exists():
        return Response({"message": f"Não foi possível concluir ação, pois o usuário {id} não existe."})


def lab_existe(id):
    if not Lab.objects.filter(id=id).exists():
        return Response({"message": f"Não foi possível concluir ação, pois o laboratório {id} não existe."})


def res_lab_existe(id):
    if not Res_Lab.objects.filter(id=id).exists():
        return Response({"message": f"Não foi possível concluir ação, pois a reserva {id} não existe."})
