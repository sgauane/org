from django.urls import path
from .views import *

urlpatterns = [
    path('org/registar/', org_register, name='org_register'),
    path('org/endereco/registar/', org_address_register, name='org_address_register'),
    path('org/avatar/', org_avatar, name='org_avatar'),
    path('org/avatar/', org_avatar, name='perfil'),
    path('org/avatar/', org_avatar, name='membro_lista'),
    path('org/remover/', org_avatar, name='org_remover'),
    path('org/editar/', org_avatar, name='org_editar'),
    path('org/detalhes/', org_show, name='org_detalhes'),
]