from django.urls import path
from .views import labs, users, resLabs, login

urlpatterns = [
    # User
    path("users/", users.getData),
    path("users/create", users.addUser),
    path("users/read/<str:pk>", users.getUser),
    path("users/update/<str:pk>", users.updateUser),
    path("users/delete/<str:pk>", users.deleteUser),
    path("users/inativar/<str:pk>", users.inativarUser),
    path("users/ativar/<str:pk>", users.ativarUser),
    # Lab
    path("labs/", labs.getData),
    path("labs/create", labs.addLab),
    path("labs/read/<str:pk>", labs.getLab),
    path("labs/update/<str:pk>", labs.updateLab),
    path("labs/delete/<str:pk>", labs.deleteLab),
    path("labs/inativar/<str:pk>", labs.inativarLab),
    path("labs/ativar/<str:pk>", labs.ativarLab),
    # ResLab
    path("resLabs/", resLabs.getData),
    path("resLabs/create", resLabs.addResLab),
    path("resLabs/read/<str:pk>", resLabs.getResLab),
    path("resLabs/update/<str:pk>", resLabs.updateResLab),
    path("resLabs/delete/<str:pk>", resLabs.deleteResLab),
    # Login
    path("login/", login.login),
]
