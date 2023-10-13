from django.urls import path
from .views import labs, res_lab, users, login, inicio
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    # Inicio
    path("", inicio.exibir_urls_view),
    # User - Privado individualmente alunos e professores
    path("users", users.get_all_users_view),
    path("users/read/<str:pk>", users.get_user_view),
    path("users/create", users.add_user_view),
    path("users/update/<str:pk>", users.update_user_view),
    path("users/delete/<str:pk>", users.delete_user_view),
    path("users/inativar/<str:pk>", users.inativar_user_view),
    path("users/ativar/<str:pk>", users.ativar_user_view),
    # Lab - Privado para professores
    path("labs", labs.get_all_labs_view),
    path("labs/read/<str:pk>", labs.get_lab_view),
    path("labs/create", labs.add_lab_view),
    path("labs/update/<str:pk>", labs.update_lab_view),
    path("labs/delete/<str:pk>", labs.delete_lab_view),
    path("labs/inativar/<str:pk>", labs.inativar_lab_view),
    path("labs/ativar/<str:pk>", labs.ativar_lab_view),
    # ResLab - Privado individualmente alunos e professores
    path("reslabs", res_lab.get_all_res_lab_view),
    path("reslabs/read/<str:pk>", res_lab.get_res_lab_view),
    path("reslabs/create", res_lab.add_res_lab_view),
    path("reslabs/update/<str:pk>", res_lab.update_res_lab_view),
    path("reslabs/delete/<str:pk>", res_lab.delete_res_lab_view),
    # Login
    path("login", login.login_user_view),
]
