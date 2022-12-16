from django.db import models

from apps.reg.models import *


# Create your models here.
def get_upload_path(instance, filename):
    print('instance:',instance.usuario_criacao, 'Filename:', filename)
    return 'imagens/projecto/susuario_{0}/{1}/'.format(instance.usuario_criacao.username, filename)

def get_upload_path_galeria(instance, filename):
    print('instance:',instance.usuario_criacao, 'Filename:', filename)
    return 'imagens/usuario_{0}/{1}/projectos'.format(instance.usuario_criacao.username, filename)


class Projecto(ModeloBase):
    designacao = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500)
    organizacao = models.ForeignKey(Organizacao, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(upload_to=get_upload_path, null=True)


class ProjectoGaleria(ModeloBase):
    projecto = models.ForeignKey(Projecto, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=get_upload_path_galeria)
    descricao = models.CharField(max_length=500, null=True, blank=True)



class Recurso(ModeloBase):
    projecto = models.ForeignKey(Projecto, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
