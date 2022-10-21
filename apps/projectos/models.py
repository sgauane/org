from django.db import models

from apps.reg.models import *


# Create your models here.
class Projecto(ModeloBase):
    designacao = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500)
    organizacao = models.ForeignKey(Organizacao, on_delete=models.SET_NULL, null=True)


class Recurso(ModeloBase):
    projecto = models.ForeignKey(Projecto, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
