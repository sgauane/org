from django.urls import path

from .views import *

#Projectos
urlpatterns = [

    # The home page
    path('projectos/', index, name='projecto_list'),
    path('projectos/detalhes/<id>', projecto_detalhes, name='projecto_detalhes'),
    path('projectos/editar/<id>', projecto_editar, name='projecto_edit'),
    path('projectos/Registar/', projecto_register, name='projecto_register'),
    path('projectos/galeria/<id>', projecto_galeria_list, name='projecto_galeria_list'),
    path('projectos/galeria/Registar/<id>', projecto_galeria_register, name='projecto_galeria_register'),

]