# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

from apps.reg.models import *


# Create your models here.
class Perguntas(ModeloBase):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    titulo = models.CharField(max_length=255)
    mensagem = models.CharField(max_length=1000)
    resposta = models.CharField(max_length=1000)
    favorito = models.BooleanField(default=False)
    # organizacao = models.ForeignKey(Organizacao, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.titulo


class SobreNos(ModeloBase):
    missao = models.CharField(max_length=255)
    visao = models.CharField(max_length=255, null=True)
    descricao = models.CharField(max_length=1000)
    organizacao = models.OneToOneField(Organizacao, on_delete=models.SET_NULL, null=True)


class Valores(ModeloBase):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE)
    designacao = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'

    def __str__(self):
        return self.designacao


class Equipa(Pessoa):
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=500)



