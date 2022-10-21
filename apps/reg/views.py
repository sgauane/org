from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.utils import timezone
from psycopg2 import Date

from apps.reg.UtilDao import UtilDao
from apps.reg.UtilEmail import UtilEmail
from apps.reg.forms import OrganizacaoForm, EnderecoForm, ImagemForm, PessoaForm, MembroForm
from apps.reg.models import Localizacao, Endereco, Organizacao, Imagem


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

            return redirect("{% url 'org_detalhes' %}")

    else:
        form = OrganizacaoForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "reg/org/form.html", data)


def org_edit(request, id):
    data = {}
    success = False
    dao = UtilDao()

    organizacao = dao.getOrg(id)

    if request.method == "POST":
        print("It's Post")
        form = OrganizacaoForm(request.POST, instance=organizacao)

        print(form.errors)
        if form.is_valid():
            user = request.user
            org = form.save(commit=False)
            org.admin_user = user
            form.save()
            success = True

            return redirect("org_detalhes")

    else:
        form = OrganizacaoForm(instance=organizacao)

    data["form"] = form
    data["success"] = success

    return render(request, "reg/org/form.html", data)


def perfil(request):
    data = {}
    dao = UtilDao()
    mail = UtilEmail()

    print("Teste de sessao request.session.org >>>> ", int(request.session.get("org")))

    # Teste de envio de emai. SUcesso
    # mail.send()

    user = request.user
    org = dao.getOrgByUser(user)
    endereco = dao.getAddressByOrg(org)

    data["organizacao"] = org
    data["endereco"] = endereco
    data["imagem"] = org.foto
    data["orgId"] = org.id

    page = "reg/perfil.html"

    return render(request,page, data)


def org_show(request):
    dao = UtilDao()
    context = {}

    user = User.objects.get(username=request.user)
    organizacao = dao.getOrgByUser(user)

    if organizacao==None:
        organizacao = Organizacao()

    context["organizacao"] = organizacao

    return render(request, "reg/org/show.html", context)

# ENDERECO
def org_address_register(request):
    data = {}
    success = False
    skip = None
    dao = UtilDao()

    if request.method == "POST":
        form = EnderecoForm(request.POST)
        print('Its POST')
        if form.is_valid():
            print('Its Valid')

            user = request.user
            org = Organizacao.objects.get(admin_user=user)
            print(org)

            # Verifica se ja tem um endereco. caso exista direciona aos detalhes
            enderecoList = dao.getAddressByOrg(org)
            if len(enderecoList) > 0:
                redirect("org_address_detalhes")

            bairro = form.cleaned_data.get("bairro")
            print("bairro", bairro.id)

            try:
                with transaction.atomic():
                    localizacao = Localizacao()

                    bairro = form.cleaned_data.get("bairro")
                    localizacao.bairro = bairro
                    localizacao.rua_avenida = form.cleaned_data.get("rua_avenida")
                    localizacao.nome_edificio = form.cleaned_data.get("nome_edificio")
                    localizacao.quarteirao = form.cleaned_data.get("quarteirao")
                    localizacao.numero_edificio = form.cleaned_data.get("numero_edificio")

                    localizacao.save()

                    # sid = transaction.savepoint() #Salvando a transacao da localizacao

                    endereco = Endereco()

                    endereco.localizacao = localizacao
                    endereco.andar = form.cleaned_data.get("andar")
                    endereco.flat = form.cleaned_data.get("flat")
                    endereco.numero_casa = form.cleaned_data.get("numero_casa")
                    endereco.entidade = org

                    endereco.save()

                    # transaction.savepoint_commit(sid) # Commit da localizacao e endereco
                    success = True

                print("saved.")
                return redirect("org_address_detalhes")
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


def org_address_edit(request, id):
    data = {}
    success = False
    dao = UtilDao()

    endereco = dao.getAddress(id)

    if request.method == "POST":
        print("It's Post")
        form = EnderecoForm(request.POST)

        print(form.errors)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # localizacao = endereco.localizacao
                    #
                    # bairro = form.cleaned_data.get("bairro")
                    # localizacao.bairro = bairro
                    # localizacao.rua_avenida = form.cleaned_data.get("rua_avenida")
                    # localizacao.nome_edificio = form.cleaned_data.get("nome_edificio")
                    # localizacao.quarteirao = form.cleaned_data.get("quarteirao")
                    # localizacao.numero_edificio = form.cleaned_data.get("numero_edificio")
                    #
                    # localizacao.save()

                    # sid = transaction.savepoint() #Salvando a transacao da localizacao

                    enderecoHistorico = Endereco()
                    enderecoHistorico.flat = endereco.flat
                    enderecoHistorico.andar = endereco.andar
                    enderecoHistorico.localizacao = endereco.localizacao
                    enderecoHistorico.entidade = endereco.entidade
                    enderecoHistorico.numero_casa = endereco.numero_casa
                    enderecoHistorico.data_fim = timezone.now()
                    enderecoHistorico.data_actualizacao = timezone.now()

                    print("<<<<<<<<<<<<.>>>>>>>>>>>>", enderecoHistorico.id)

                    # endereco.localizacao = localizacao
                    endereco.id = id
                    endereco.andar = form.cleaned_data.get("andar")
                    endereco.flat = form.cleaned_data.get("flat")
                    endereco.numero_casa = form.cleaned_data.get("numero_casa")
                    endereco.data_actualizacao = timezone.now()
                    # endereco.entidade = org

                    print("fddgdfgdfgd>>",endereco.id)
                    enderecoHistorico.save()
                    endereco.save()


                    # transaction.savepoint_commit(sid) # Commit da localizacao e endereco
                    success = True

                print("saved.")
                return redirect("org_address_detalhes")
            except Exception as e:
                print(e)
                # transaction.savepoint_rollback(sid)
                transaction.rollback()

    else:
        form = EnderecoForm({
            "cidade": endereco.localizacao.bairro.cidade,
            "bairro": endereco.localizacao.bairro,
            "rua_avenida": endereco.localizacao.rua_avenida,
            "nome_edificio":endereco.localizacao.nome_edificio,
            "quarteirao": endereco.localizacao.quarteirao,
            "numero_edificio": endereco.localizacao.numero_edificio,
            "andar": endereco.andar,
            "flat": endereco.flat,
            "numero_casa": endereco.numero_casa
        })



    data["form"] = form
    data["success"] = success

    return render(request, "reg/endereco/form.html", data)

def org_address_show(request):
    dao = UtilDao()
    context = {}

    user = User.objects.get(username=request.user)
    organizacao = dao.getOrgByUser(user)
    enderecoList = dao.getAddressByOrg(organizacao)
    endereco = enderecoList.first

    if endereco==None:
        print("Endereco vazio")
        endereco = Endereco()
    print(endereco)

    context["endereco"] = endereco

    return render(request, "reg/endereco/show.html", context)


#Imagem
def imagem_registar(request):
    data = {}
    success = False
    skip = None
    user = request.user

    if request.method == "POST":
        form = ImagemForm(request.POST, request.FILES)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            print('Its Valid')

            org = Organizacao.objects.get(admin_user=user.id)
            print(org)

            try:
                with transaction.atomic():
                    avatar = form.save()
                    org.foto = avatar
                    org.save()
                    success = True

                print("saved.")
                return redirect("perfil")
            except Exception as e:
                print('error >>>',e)
                # transaction.savepoint_rollback(sid)
                transaction.rollback()

        print('Its Not Valid')

    else:
        imagemInstance = Imagem()
        imagemInstance.usuario_criacao = user
        form = ImagemForm(instance=imagemInstance)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request,'reg/imagem/form.html', data)


def imagem_show(request, id):
    dao = UtilDao()
    context = {}

    imagem = dao.getImagem(id)

    context["imagem"] = imagem

    return render(request, "reg/imagem/show.html", context)


def imagem_editar(request, id):
    data = {}
    success = False
    dao = UtilDao()

    img = dao.getImagem(id)

    if request.method == "POST":
        form = ImagemForm(request.POST, request.FILES, instance=img)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            print('Its Valid')

            try:
                with transaction.atomic():
                    avatar = form.save()
                    success = True

                print("saved.")
                return redirect("perfil")
            except Exception as e:
                print('error >>>', e)
                # transaction.savepoint_rollback(sid)
                transaction.rollback()

        print('Its Not Valid')

    else:
        form = ImagemForm(instance=img)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request, 'reg/imagem/form.html', data)


#Pessoa
def pessoa_registar(request):
    data = {}
    success = False

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            p = form.save()
            success = True

            return redirect("pessoa_detalhes", id=p.id)

    else:
        form = PessoaForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "reg/pessoa/form.html", data)


def pessoa_show(request, id):
    dao = UtilDao()
    context = {}

    pessoa = dao.getPessoa(id)

    context["pessoa"] = pessoa

    return render(request, "reg/pessoa/show.html", context)


def pessoa_registar(request):
    data = {}
    success = False

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            p = form.save()
            success = True

            return redirect("pessoa_detalhes", id=p.id)

    else:
        form = PessoaForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "reg/pessoa/form.html", data)


def pessoa_editar(request, id):
    data = {}
    success = False
    dao = UtilDao()

    p = dao.getPessoa(id)

    if request.method == "POST":
        form = PessoaForm(request.POST, instance=p)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            form.save()
            print(p.id)
            return redirect("pessoa_detalhes", id=p.id)


        print('Its Not Valid')

    else:
        form = PessoaForm(instance=p)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request, 'reg/pessoa/form.html', data)


#Membro
def membro_list(request):
    dao = UtilDao()
    context = {}

    orgId = request.session.get("org")

    membros = dao.findAllMembrosByOrg(orgId)

    context["membros"] = membros
    context["orgId"] = orgId

    return render(request, "reg/membro/list.html", context)


def membro_registar(request, orgId):
    data = {}
    success = False
    dao = UtilDao()
    user = request.user

    org = dao.getOrg(orgId)
    mc = dao.getModificadorContrato(1) #Inicial

    if request.method == "POST":
        form = MembroForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)

            obj.contratante = org
            obj.modificador = mc
            obj.usuario_criacao = user

            obj = form.save()
            success = True

            return redirect("membro_detalhes", id=obj.id)

    else:
        form = MembroForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "reg/membro/form.html", data)


def membro_show(request, id):
    dao = UtilDao()
    context = {}

    pessoa = dao.getMembro(id)

    context["instance"] = pessoa

    return render(request, "reg/membro/show.html", context)


def membro_editar(request, id):
    data = {}
    success = False
    dao = UtilDao()

    obj = dao.getMembro(id)

    if request.method == "POST":
        form = MembroForm(request.POST, instance=obj)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("membro_detalhes", id=obj.id)


        print('Its Not Valid')

    else:
        form = MembroForm(instance=obj)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request, 'reg/membro/form.html', data)