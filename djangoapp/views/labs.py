from rest_framework.decorators import api_view, permission_classes
from ..permissions import Cadastrado, IsProfessorOrAdmin, Admin
from ..controllers import labs_controller


@api_view(["GET"])
@permission_classes([Cadastrado])
def get_all_labs_view(request):
    return labs_controller.get_all_labs(request)


@api_view(["GET"])
@permission_classes([Cadastrado])
def get_lab_view(request, pk):
    return labs_controller.get_lab(request, pk)


@api_view(["POST"])
@permission_classes([Admin])
def add_lab_view(request):
    return labs_controller.add_lab(request)


@api_view(["PUT"])
@permission_classes([Admin])
def inativar_lab_view(request, pk):
    return labs_controller.inativar_lab(request, pk)


@api_view(["PUT"])
@permission_classes([Admin])
def ativar_lab_view(request, pk):
    return labs_controller.ativar_lab(request, pk)


@api_view(["PUT"])
@permission_classes([Admin])
def update_lab_view(request, pk):
    return labs_controller.update_lab(request, pk)


@api_view(["DELETE"])
@permission_classes([Admin])
def delete_lab_view(request, pk):
    return labs_controller.delete_lab(request, pk)
