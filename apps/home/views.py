# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from apps.home.forms import PerguntaForms, SobreNosForm, ValoresForm
from apps.reg.UtilDao import UtilDao


@login_required(login_url="/entrar/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def h(request):
    context = {'segment': 'c_home',
               'titulo': 'Bem vindo'}

    html_template = loader.get_template('home/welcome.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def sitio_inicio(request):
    context = {}
    dao = UtilDao()
    user = request.user
    orgId = request.session.get("org")
    print("User: ", user)

    if request.method == "POST" :

        form = PerguntaForms(request.POST)

        if form.is_valid():
            if user is not None:
                p = form.save(commit=False)
                p.usuario_criacao = user

            form.save()
            print("sitio_inicio >>> Saved.")
            return redirect("sitio_inicio")

    form = PerguntaForms()
    faqs = dao.findAllPerguntasFrequentes()
    sobrenos = dao.getSobreNosByOrg(orgId=orgId)
    valores = dao.findAllValoresByOrg(orgId)
    projectos = dao.findAllProjectosByOrg(orgId)

    print("Perguntas:", len(faqs))

    context["form"] = form
    context["faqs"] = faqs
    context["sobrenos"] = sobrenos
    context["valores"] = valores
    context["projectos"] = projectos

    html_template = loader.get_template('sitio/index.html')
    return HttpResponse(html_template.render(context, request))


def perguntas_list(request):
    dao = UtilDao()
    context = {}

    # orgId = request.session.get("org")

    lista = dao.findAllPerguntas()

    context["perguntas"] = lista

    return render(request, "home/perguntas/list.html", context)

def sobrenos_registar(request):
    data = {}
    success = False
    dao = UtilDao()
    user = request.user

    org = dao.getOrgByUser(user)

    if request.method == "POST":
        form = SobreNosForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_criacao = user
            obj.organizacao = org
            obj = form.save()
            success = True

            return redirect("sobrenos_detalhes")

    else:
        form = SobreNosForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "home/about/form.html", data)

def sobrenos_show(request):
    dao = UtilDao()
    context = {}

    orgId = request.session.get("org")
    org = dao.getOrg(orgId)
    pessoa = dao.getSobreNosByOrg(org)

    context["instance"] = pessoa

    return render(request, "home/about/show.html", context)

def sobrenos_editar(request):
    data = {}
    success = False
    dao = UtilDao()

    orgId = request.session.get("org")
    obj = dao.getSobreNosByOrg(orgId)

    if request.method == "POST":
        form = SobreNosForm(request.POST, instance=obj)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("sobrenos_detalhes", id=obj.id)


        print('Its Not Valid')

    else:
        form = SobreNosForm(instance=obj)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request, 'home/about/form.html', data)

def valores_registar(request):
    data = {}
    success = False
    dao = UtilDao()
    user = request.user

    org = dao.getOrgByUser(user)

    if request.method == "POST":
        form = ValoresForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario_criacao = user
            obj.organizacao = org
            obj = form.save()
            success = True

            return redirect("valores_detalhes", id=obj.id)

    else:
        form = ValoresForm(request.POST or None)

    data["form"] = form
    data["success"] = success

    print("render to form")
    return render(request, "home/valores/form.html", data)

def valores_show(request, id):
    dao = UtilDao()
    context = {}

    pessoa = dao.getValores(id)

    context["instance"] = pessoa

    return render(request, "home/valores/show.html", context)

def valores_editar(request, id):
    data = {}
    success = False
    dao = UtilDao()

    obj = dao.getValores(id)

    if request.method == "POST":
        form = ValoresForm(request.POST, instance=obj)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("valores_detalhes", id=obj.id)


        print('Its Not Valid')

    else:
        form = ValoresForm(instance=obj)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request, 'home/valores/form.html', data)

def valores_list(request):
    dao = UtilDao()
    context = {}

    orgId = request.session.get("org")

    lista = dao.findAllValoresByOrg(orgId)

    context["lista"] = lista

    return render(request, "home/valores/list.html", context)

def projectos_list(request):
    dao = UtilDao()
    context = {}

    orgId = request.session.get("org")

    lista = dao.findAllProjectosByOrg(orgId)

    context["lista"] = lista

    return render(request, "home/valores/list.html", context)

def projecto_galeria(request, id):
    dao = UtilDao()
    context = {}

    lista = dao.findAllGaleriaByProjecto(id)

    context["lista"] = lista

    return render(request, "sitio/projecto-galeria.html", context)


