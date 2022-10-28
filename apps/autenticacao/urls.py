from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.autenticacao.views import login_view, register_user

urlpatterns = [
    path('entrar/', login_view, name="login"),
    path('registar/', register_user, name="register"),
    path('sair/', LogoutView.as_view(), name="logout"),
]