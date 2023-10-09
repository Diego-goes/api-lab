from rest_framework.decorators import api_view, permission_classes
from ..permissions import Cadastrado, IsProfessorOrAdmin
from ..controllers import res_lab_controller

@api_view(["GET"])
@permission_classes([Cadastrado])
def get_all_res_lab_view(request):
    return res_lab_controller.get_all_res_lab(request)


@api_view(["GET"])
@permission_classes([Cadastrado])
def get_res_lab_view(request, pk):
    return res_lab_controller.get_res_lab(request, pk)


@api_view(["POST"])
@permission_classes([Cadastrado])
def add_res_lab_view(request):
    return res_lab_controller.add_res_Lab(request)


@api_view(["PUT"])
@permission_classes([Cadastrado])
def update_res_lab_view(request, pk):
    return res_lab_controller.update_res_lab(request, pk)


@api_view(["DELETE"])
@permission_classes([Cadastrado])
def delete_res_lab_view(request, pk):
    return res_lab_controller.delete_res_lab(request,pk)