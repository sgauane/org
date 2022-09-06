from django.urls import path
from .views import *

urlpatterns = [
    path('org/registar/', org_register, name='org_register'),
    path('org/endereco/registar/', org_address_register, name='org_address_register'),
    path('org/avatar/', org_avatar, name='org_avatar'),
]