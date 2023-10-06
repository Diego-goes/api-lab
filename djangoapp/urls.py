from django.urls import path
from .views import labs, users, resLabs, login, inicio
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Inicio
    path("", inicio.exibirUrls),
    # User - Privado individualmente alunos e professores
    path("users/", users.getData),
    path("users/create", users.addUser),
    path("users/read/<str:pk>", users.getUser),
    path("users/update/<str:pk>", users.updateUser),
    path("users/delete/<str:pk>", users.deleteUser),
    path("users/inativar/<str:pk>", users.inativarUser),
    path("users/ativar/<str:pk>", users.ativarUser),
    # Lab - Privado para professores
    path("labs/", labs.getData),
    path("labs/create", labs.addLab),
    path("labs/read/<str:pk>", labs.getLab),
    path("labs/update/<str:pk>", labs.updateLab),
    path("labs/delete/<str:pk>", labs.deleteLab),
    path("labs/inativar/<str:pk>", labs.inativarLab),
    path("labs/ativar/<str:pk>", labs.ativarLab),
    # ResLab - Privado individualmente alunos e professores
    path("reslabs/", resLabs.getData),
    path("reslabs/create", resLabs.addResLab),
    path("reslabs/read/<str:pk>", resLabs.getResLab),
    path("reslabs/update/<str:pk>", resLabs.updateResLab),
    path("reslabs/delete/<str:pk>", resLabs.deleteResLab),
    # Login
    path("login/", login.login),
]
