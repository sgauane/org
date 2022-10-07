from django.urls import path

from .views import *

urlpatterns = [
    path('org/registar/', org_register, name='org_register'),
    path('org/detalhes/', org_show, name='org_detalhes'),
    path('org/editar/<id>', org_edit, name='org_edit'),
    path('org/endereco/registar/', org_address_register, name='org_address_register'),
    path('org/endereco/detalhes/', org_address_show, name='org_address_detalhes'),
    path('org/endereco/editar/<int:id>', org_address_edit, name='org_address_edit'),
    path('imagem/registar/', imagem_registar, name='imagem_register'),
    path('imagem/detalhes/<int:id>', imagem_show, name='imagem_detalhes'),
    path('imagem/editar/<int:id>', imagem_editar, name='imagem_edit'),
    path('org/avatar/', imagem_registar, name='perfil'),
    path('org/avatar/', imagem_registar, name='membro_lista'),
    # path('org/remover/', imagem_registar, name='org_remover'),
    # path('org/editar/', imagem_registar, name='org_editar'),

]