from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.autenticacao.forms import LoginForm, SignUpForm
from apps.autenticacao.models import Token
from apps.autenticacao.token import genToken, saveToken
from core.util import send_email


# Create your views here.
def login_view(request):
    data = {}
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

    data["form"] = form
    return render(request, "account/login.html", data)


def register_user(request):
    data = {}
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            success = True

            #compose token and save
            print('compose token')
            tk = saveToken(user)
            send_email(request)
            print('email sent')

            return redirect('/entrar/')

    else:
        form = SignUpForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "account/register.html", data)


def confirm_registration(request, token):
    data = {}
    msg = ""
    link_home = ""

    try:
        #Buscar registo do token a partir do codigo enviado pelo email
        tk = Token.objects.get(token=token)

        #Buscar o Usuario desse token
        user = User.objects.get(pk=tk.user.id)

        #Activar o ususario
        user.is_active = True
        user.save()

        #Remover o token
        tk.delete()

        msg = "Registo activado com sucesso"
        link_home = "Ir para a pagina inicial"

    except Exception as e:
        msg = "Erro ao confirmar registo" + str(e)
        print(msg)
        #Encaminhar para o erro de validacao

    data["msg"] = msg
    data["link_home"] = link_home

    render(request, 'Pagina de activacao do registo', data)


def sendEmail(user):
    _from = ""
    _to = user.email
    _subject = ""
    _message = ""