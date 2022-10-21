# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

from apps.reg.models import *


# Create your models here.
class Perguntas:
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    titulo = models.CharField(max_length=255)
    mensagem = models.CharField(max_length=1000)
    resposta = models.CharField(max_length=1000)
    # organizacao = models.ForeignKey(Organizacao, on_delete=models.SET_NULL)


class SobreNos(ModeloBase):
    titulo = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    texto = models.CharField(max_length=1000)
    organizacao = models.ForeignKey(Organizacao, on_delete=models.SET_NULL, null=True)




class Equipa(Pessoa):
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=500)



