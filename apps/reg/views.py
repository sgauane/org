from django.db import transaction
from django.shortcuts import render, redirect

from apps.reg.forms import OrganizacaoForm, EnderecoForm, ImagemForm
from apps.reg.models import Localizacao, Endereco, Organizacao


# Create your views here.

# ORGANIZACAO
def org_register(request):
    data = {}
    success = False

    if request.method == "POST":
        form = OrganizacaoForm(request.POST)

        if form.is_valid():
            user = request.user
            org = form.save(commit=False)
            org.admin_user = user
            form.save()
            success = True

            return redirect('/endereco/')

    else:
        form = OrganizacaoForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "reg/org/form.html", data)


# ENDERECO
def org_address_register(request):
    data = {}
    success = False
    skip = None

    if request.method == "POST":
        form = EnderecoForm(request.POST)
        print('Its POST')
        if form.is_valid():
            print('Its Valid')

            user = request.user
            org = Organizacao.objects.get(admin_user=user.id)
            print(org)

            bairro = form.cleaned_data.get("bairro")
            print("bairro", bairro.id)

            try:
                with transaction.atomic():
                    localizacao = Localizacao()
                    bairro = form.cleaned_data.get("bairro")
                    localizacao.bairro = bairro
                    localizacao.rua_avenida = form.cleaned_data.get("rua_avenida")
                    localizacao.nome_edificio = form.cleaned_data.get("nome_edificio")
                    localizacao.numero_edificio = form.cleaned_data.get("numero_edificio")

                    localizacao.save()

                    # sid = transaction.savepoint() #Salvando a transacao da localizacao

                    endereco = Endereco()

                    endereco.localizacao = localizacao
                    endereco.ander = form.cleaned_data.get("andar")
                    endereco.flat = form.cleaned_data.get("flat")
                    endereco.numero_casa = form.cleaned_data.get("numero_casa")
                    endereco.entidade = org

                    endereco.save()

                    # transaction.savepoint_commit(sid) # Commit da localizacao e endereco
                    success = True

                print("saved.")
                return redirect("{% url 'org_avatar'  %}")
            except Exception as e:
                print(e)
                # transaction.savepoint_rollback(sid)
                transaction.rollback()






        print('Its Not Valid')

    else:
        form = EnderecoForm(request.POST or None)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip

    return render(request, "reg/endereco/form.html", data)

#Imagem
def org_avatar(request):
    data = {}
    success = False
    skip = None

    if request.method == "POST":
        form = ImagemForm(request.POST, request.FILES)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            print('Its Valid')

            user = request.user
            org = Organizacao.objects.get(admin_user=user.id)
            print(org)

            try:
                with transaction.atomic():
                    avatar = form.save()
                    success = True

                print("saved.")
                return redirect("{% url 'avatar'  %}")
            except Exception as e:
                print(e)
                # transaction.savepoint_rollback(sid)
                transaction.rollback()

        print('Its Not Valid')

    else:
        form = ImagemForm()
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request,'reg/imagem/form.html', data)
