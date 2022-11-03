from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, View
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .models import Asignar_asesoria, Capacitacion,Visita, Solicitar_asesoria, Checklist, Usuario, Profesional, Contrato
from .forms import  CapacitacionForm, UsuarioModelForm, VisitaForm, SolicitarasesoriaForm, Asignar_asesoriaForm, ChecklistForm, ProfesionalForm, ContratoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as ingresar, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def servicios(request):
    return render(request, "core/servicios.html")

def login(request):
    return render(request, "core/login.html")

def registro(request):   
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} Creado')
    else:
        form = UsuarioModelForm()
    
    context = {'form' : form }
    return render(request,'core/Registros/registro.html', context)
        

def registrar_usuario(request):
    if request.method == "POST" : 
        form = UsuarioModelForm(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request, "creado correctamente")
            return redirect('aseguradoraNMA:index')
    else :
            form = UsuarioModelForm()
    return render(request , 'core/Registros/registrar_usuario.html' , {'form' : form})


def mantenedor_usuario(request):
    usuario = Usuario.objects.all()
    context = {
        'usuario' : usuario
    } 
    return render(request, 'core/Mantenedores/mantenedor_usuario.html', context)

def detalle_usuario(request , id) :
    detalle_usuario = get_object_or_404(Usuario , pk = id)
    context = {
        'detalle_usuario' : detalle_usuario
    }
    return render(request ,'core/Mantenedores/detalle_usuario.html', context)

#def detalle_cliente(request , id) :
#    detalle_cliente = get_object_or_404(Usuario , pk = id)
#    context = {
#        'detalle_cliente' : detalle_cliente
#    }
#    return render(request ,'core/Cliente/detalle_cliente.html', context)

def crear_usuario(request) :
    if request.method == "POST" : 
        form = UsuarioModelForm(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request, "creado correctamente")
            return redirect('aseguradoraNMA:mantenedor_usuario')
    else :
            form = UsuarioModelForm()
    return render(request , 'core/Mantenedores/crear_usuario.html' , {'form' : form})

def editar_usuario(request , id) :
    usuario = get_object_or_404(Usuario , id = id)
    data = {
        'form': UsuarioModelForm(instance=usuario)
    }

    if request.method == "POST" :
        usuario_form = UsuarioModelForm(data=request.POST , instance=usuario, files=request.FILES)
        if usuario_form.is_valid() :
            usuario_form.save()
            messages.success(request, "modificado correctamente")
            return redirect('aseguradoraNMA:mantenedor_usuario')
        data["form"] = usuario_form

    return render(request, 'core/Mantenedores/editar_usuario.html', data)
    
def eliminar_usuario(request , id) :
    usuario = get_object_or_404(Usuario , id = id)

    if usuario : 
        usuario.delete()
        messages.success(request, "eliminado correctamente")
        return redirect('aseguradoraNMA:mantenedor_usuario')

#LISTADO DE PROFESIONALES
def mantenedor_profesional(request):
    profesional = Profesional.objects.all()
    context = {
        'profesional' : profesional
    } 
    return render(request, 'core/Mantenedores/mantenedor_profesional.html', context)

#def detalle_usuario(request , id) :
#    detalle_usuario = get_object_or_404(Usuario , pk = id)
#    context = {
#        'detalle_usuario' : detalle_usuario
#    }
#    return render(request ,'core/Mantenedores/detalle_usuario.html', context)

def crear_profesional(request) :
    if request.method == "POST" : 
        form = ProfesionalForm(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request, "creado correctamente")
            return redirect('aseguradoraNMA:mantenedor_profesional')
    else :
            form = ProfesionalForm()
    return render(request , 'core/Mantenedores/crear_profesional.html' , {'form' : form})

def editar_profesional(request , id) :
    profesional = get_object_or_404(Profesional , id = id)
    data = {
        'form': ProfesionalForm(instance=profesional)
    }

    if request.method == "POST" :
        form = ProfesionalForm(data=request.POST , instance=profesional, files=request.FILES)
        if form.is_valid() :
            form.save()
            messages.success(request, "modificado correctamente")
            return redirect('aseguradoraNMA:mantenedor_profesional')
        data["form"] = form

    return render(request, 'core/Mantenedores/editar_profesional.html', data)
    
def eliminar_profesional(request , id) :
    profesional = get_object_or_404(Profesional , id = id)

    if profesional : 
        profesional.delete()
        messages.success(request, "eliminado correctamente")
        return redirect('aseguradoraNMA:mantenedor_profesional')

#CAPACITACIONES
def crear_capacitacion(request):

    data = {
        'form': CapacitacionForm()
    }
    if request.method == "POST" : 
        formulario = CapacitacionForm(request.POST)
        if formulario.is_valid() : 
            formulario.save()
            messages.success(request, "creada correctamente")
            return redirect('aseguradoraNMA:listar_capacitacion')
    return render(request, 'core/Capacitaciones/crear_capacitacion.html', data)

def listar_capacitacion(request):
    capacitaciones = Capacitacion.objects.all()
    data = {
        'capacitaciones' : capacitaciones
    }
    return render(request, 'core/Capacitaciones/listar_capacitacion.html', data)

def editar_capacitacion(request, id):

    capacitaciones = get_object_or_404(Capacitacion, id=id)

    data = {
        'form': CapacitacionForm(instance=capacitaciones)
    }

    if request.method == 'POST':
        formulario = CapacitacionForm(data=request.POST, instance=capacitaciones, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect('aseguradoraNMA:listar_capacitacion')
        data["form"] = formulario

    return render(request, 'core/Capacitaciones/editar_capacitacion.html',data)

def eliminar_capacitacion(request, id):
    capacitaciones = get_object_or_404(Capacitacion, id=id)
    capacitaciones.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('aseguradoraNMA:listar_capacitacion')

#PLANIFICAR VISITA
def planificar_visita(request):

    data = {
        'form': VisitaForm()
    }
    if request.method == "POST" : 
        formulario = VisitaForm(request.POST)
        if formulario.is_valid() : 
            formulario.save()
            messages.success(request, "registrado correctamente")
            return redirect('aseguradoraNMA:mantenedor_visita')
    return render(request, 'core/Visitas/planificar_visita.html', data)

def listar_visita(request):
    visitas = Visita.objects.all()
    data = {
        'visitas' : visitas
    }
    return render(request, 'core/Visitas/mantenedor_visita.html', data)

def editar_visita(request, id):

    visitas = get_object_or_404(Visita, id=id)

    data = {
        'form': VisitaForm(instance=visitas)
    }

    if request.method == 'POST':
        formulario = VisitaForm(data=request.POST, instance=visitas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "editado correctamente")
            return redirect('aseguradoraNMA:mantenedor_visita')
        data["form"] = formulario

    return render(request, 'core/Visitas/editar_visita.html',data)

def eliminar_visita(request, id):
    visitas = get_object_or_404(Visita, id=id)
    visitas.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('aseguradoraNMA:mantenedor_visita')

def mantenedor_checklist(request):
    checklist = Checklist.objects.all()
    data = {
        'checklist' : checklist
    }
    return render(request, 'core/Visitas/mantenedor_checklist.html', data)

def crear_checklist(request):

    data = {
        'form': ChecklistForm()
    }
    if request.method == "POST" : 
        formulario = ChecklistForm(request.POST)
        if formulario.is_valid() : 
            formulario.save()
            messages.success(request, "creado correctamente")
    return render(request, 'core/Visitas/crear_checklist.html', data)

def editar_checklist(request , id) :
    checklist = get_object_or_404(Checklist , id = id)
    data = {
        'form': ChecklistForm(instance=checklist)
    }

    if request.method == "POST" :
        form = ChecklistForm(data=request.POST , instance=checklist, files=request.FILES)
        if form.is_valid() :
            form.save()
            messages.success(request, "modificado correctamente")
            return redirect('aseguradoraNMA:mantenedor_checklist')
        data["form"] = form

    return render(request, 'core/Visitas/editar_checklist.html', data)
    
def eliminar_checklist(request , id) :
    checklist = get_object_or_404(Checklist , id = id)

    if checklist : 
        checklist.delete()
        messages.success(request, "eliminado correctamente")
        return redirect('aseguradoraNMA:mantenedor_checklist')

#SOLICITAR ASESORIAS

def solicitar_asesoria(request):

    data = {
        'form': SolicitarasesoriaForm()
    }
    if request.method == "POST" : 
        formulario = SolicitarasesoriaForm(request.POST)
        if formulario.is_valid() : 
            formulario.save()
            messages.success(request, "solicitud ingresada")
    return render(request, 'core/Asesorias/solicitar_asesoria.html', data)

def mantenedor_asesoria(request):
    asesorias = Solicitar_asesoria.objects.all()
    data = {
        'asesorias' : asesorias
    }
    return render(request, 'core/Asesorias/mantenedor_asesoria.html', data)

def editar_asesoria(request, id):
    asesorias = get_object_or_404(Solicitar_asesoria, id=id)

    data = {
        'form': SolicitarasesoriaForm(instance=asesorias)
    }

    if request.method == 'POST':
        formulario = SolicitarasesoriaForm(data=request.POST, instance=asesorias, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "editado correctamente")
            return redirect('aseguradoraNMA:mantenedor_asesoria')
        data["form"] = formulario

    return render(request, 'core/Asesorias/editar_asesoria.html',data)


def eliminar_asesoria(request, id):
    asesorias = get_object_or_404(Solicitar_asesoria, id=id)
    asesorias.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('aseguradoraNMA:mantenedor_asesoria')


def responder_asesoria(request):

    data = {
        'form': Asignar_asesoriaForm()
    }
    if request.method == "POST" : 
        formulario = Asignar_asesoriaForm(request.POST)
        if formulario.is_valid() : 
            formulario.save()
            messages.success(request, "registrado correctamente")
    return render(request, 'core/Asesorias/responder_asesoria.html', data)

def control_asesoria(request):
    asesorias = Asignar_asesoria.objects.all()
    data = {
        'asesorias' : asesorias
    }
    return render(request, 'core/Asesorias/asesorias_respondidas.html', data)

def detalle_asesoria(request , id) :
    detalle_asesoria = get_object_or_404(Solicitar_asesoria , pk = id)
    context = {
        'detalle_asesoria' : detalle_asesoria
    }
    return render(request ,'core/Asesorias/detalle_asesoria.html', context)

def editar_asesoria2(request, id):
    asesorias = get_object_or_404(Asignar_asesoria, id=id)

    data = {
        'form': Asignar_asesoriaForm(instance=asesorias)
    }

    if request.method == 'POST':
        formulario = Asignar_asesoriaForm(data=request.POST, instance=asesorias, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "editado correctamente")
            return redirect('aseguradoraNMA:asesorias_respondidas')
        data["form"] = formulario

    return render(request, 'core/Asesorias/editar_asesoria.html',data)


def eliminar_asesoria2(request, id):
    asesorias = get_object_or_404(Asignar_asesoria, id=id)
    asesorias.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('aseguradoraNMA:mantenedor_asesoria')

#CONTRATOS
def registrar_contrato(request):

    data = {
        'form': ContratoForm()
    }
    if request.method == "POST" : 
        formulario = ContratoForm(request.POST)
        if formulario.is_valid() : 
            formulario.save()
            messages.success(request, "contrato ingresado")
    return render(request, 'core/Contratos/registrar_contrato.html', data)

def mantenedor_contrato(request):
    contratos = Contrato.objects.all()
    data = {
        'contratos' : contratos
    }
    return render(request, 'core/Contratos/mantenedor_contrato.html', data)

def editar_contrato(request, id):
    contratos = get_object_or_404(Contrato, id=id)

    data = {
        'form': ContratoForm(instance=contratos)
    }

    if request.method == 'POST':
        formulario = ContratoForm(data=request.POST, instance=contratos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "editado correctamente")
            return redirect('aseguradoraNMA:mantenedor_contrato')
        data["form"] = formulario

    return render(request, 'core/Contratos/editar_contrato.html',data)


def eliminar_contrato(request, id):
    contratos = get_object_or_404(Contrato, id=id)
    contratos.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('aseguradoraNMA:mantenedor_contrato')