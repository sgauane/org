# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *

urlpatterns = [

    # The home page
    path('dashboard/', index, name='home'),
    path('h/', h, name='h'),
    path('', sitio_inicio, name='sitio_inicio'),
    path('site/perguntas/listar/', perguntas_list, name='perguntas_list'),
    path('site/sobrenos/registar/', sobrenos_registar, name='sobrenos_register'),
    path('site/sobrenos/detalhes/', sobrenos_show, name='sobrenos_detalhes'),
    path('site/sobrenos/editar/<id>', sobrenos_editar, name='sobrenos_edit'),
    path('site/valores/listar/', valores_list, name='valores_list'),
    path('site/valores/registar/', valores_registar, name='valores_register'),
    path('site/valores/detalhes/<id>', valores_show, name='valores_detalhes'),
    path('site/valores/editar/<id>', valores_editar, name='valores_edit'),
    path('site/valores/editar/<id>', valores_editar, name='valores_edit'),
    path('site/projectos/galeria/<id>', projecto_galeria, name='projecto_galeria'),

    # Matches any html file
    re_path(r'^.*\.*', pages, name='pages'),

]
