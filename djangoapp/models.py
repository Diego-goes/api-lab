from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=250,default='', unique=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    user_type_id = models.IntegerField(default=0)
    password = models.CharField(
        max_length=128
    )  # Use um campo apropriado para senhas, como PasswordField em produção
    is_active = models.IntegerField(default=0)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=10)
    USERNAME_FIELD = 'username'

class Lab(models.Model):
    andar = models.IntegerField(default=1)
    lab = models.CharField(max_length=250)
    is_active = models.IntegerField(default=0)
    description = models.TextField()


class Res_Lab(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default = 0)
    lab_id = models.ForeignKey(Lab, on_delete=models.CASCADE, default = 0)
    res_date = models.DateTimeField(default=datetime.now)
