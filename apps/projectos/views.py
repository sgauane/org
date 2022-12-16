from django.shortcuts import render, redirect

from apps.projectos.forms import ProjectoForms, ProjectoGaleriaForms
from apps.projectos.models import Projecto
from apps.reg.UtilDao import UtilDao
from apps.reg.models import Imagem


# Create your views here.
def index(request):
    data = {}
    dao = UtilDao()

    orgId = request.session.get("org")
    lista = dao.findAllProjectosByOrg(orgId)

    data["lista"] = lista

    return render(request,"projectos/projecto/list.html", data)

def projecto_detalhes(request, id):
    dao = UtilDao()
    context = {}

    instance = dao.getProjecto(id)

    if instance==None:
        endereco = Projecto()

    context["instance"] = instance

    return render(request, "projectos/projecto/show.html", context)


def projecto_register(request):
    data = {}
    success = False
    dao = UtilDao()
    user = request.user
    orgId = request.session.get("org")

    org = dao.getOrg(orgId)

    if request.method == "POST":
        form = ProjectoForms(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.usuario_criacao = user
            obj.organizacao = org

            obj = form.save()
            success = True

            return redirect("projecto_detalhes", id=obj.id)

    else:
        form = ProjectoForms(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "projectos/projecto/form.html", data)

def projecto_editar(request, id):
    data = {}
    success = False
    dao = UtilDao()

    obj = dao.getProjecto(id)

    if request.method == "POST":
        form = ProjectoForms(request.POST, instance=obj)
        print('Its POST')
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("projecto_detalhes", id=obj.id)


        print('Its Not Valid')

    else:
        form = ProjectoForms(instance=obj)
        skip = "Pular"

    data["form"] = form
    data["success"] = success
    data["skip"] = skip
    return render(request, 'projectos/projecto/form.html', data)

def projecto_galeria_list(request, id):
    data = {}
    dao = UtilDao()

    # orgId = request.session.get("org")
    lista = dao.findAllGaleriaByProjecto(id)

    data["lista"] = lista
    data["id"] = id

    return render(request, "projectos/galeria/list.html", data)

def projecto_galeria_register(request, id):
    data = {}
    success = False
    dao = UtilDao()
    user = request.user

    projecto = dao.getProjecto(id)

    if request.method == "POST":
        form = ProjectoGaleriaForms(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save(commit=False)
            obj.usuario_criacao = user
            obj.projecto = projecto

            obj = form.save()
            success = True

            return redirect("projecto_galeria_list", id=id)

    else:
        form = ProjectoGaleriaForms(request.POST or None)

    data["form"] = form
    data["success"] = success

    return render(request, "projectos/galeria/form.html", data)
