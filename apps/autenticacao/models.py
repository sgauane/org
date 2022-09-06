from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Token(models.Model):
    ususario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    token = models.CharField(max_length=10)
    data_criacao = models.DateField(auto_now_add=True)
    deta_validade = models.DateField()