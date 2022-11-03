from django.forms import ModelForm, Form
from .models import Capacitacion, Visita, Solicitar_asesoria, Asignar_asesoria, Checklist, Usuario, Profesional, Contrato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#class CustomUserCreationForm(UserCreationForm):
#    class Meta:
#        model = User
#        fields =  ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UsuarioModelForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields =  ['username', 'first_name', 'last_name', 'email','rut','nombre_empresa','direccion','telefono','rubro',
        'password1', 'password2']
        helps_texts = {k:"" for k in fields}


class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre_prof','apellido_prof','correo_prof','telefono_prof']

class CapacitacionForm(ModelForm):
    class Meta:
        model = Capacitacion
        fields = ['fecha_capacitacion', 'hora_capacitacion', 'asistentes_capacitacion', 'materiales_capacitacion',
        'capacitacion_extra', 'monto_capacitacion', 'fecha_termino_capacitacion', 'hora_termino_capacitacion',
        'Usuario', 'Profesional']
        widgets = {
            "fecha_capacitacion": forms.SelectDateWidget(),
            "fecha_termino_capacitacion": forms.SelectDateWidget(),
            "hora_capacitacion": forms.TimeInput()
        }

class VisitaForm(ModelForm):
    class Meta:
        model = Visita
        fields = ['fecha_inicio', 'fecha_termino', 'hora_inicio', 'hora_termino',
        'visita_extra','Usuario', 'Profesional']
        widgets = {
            "fecha_inicio": forms.SelectDateWidget(),
            "fecha_termino": forms.SelectDateWidget(),
            "hora_inicio": forms.TimeInput(),
            "hora_termino": forms.TimeInput(),
        }


class SolicitarasesoriaForm(ModelForm):
    class Meta:
        model = Solicitar_asesoria
        fields = ['fecha_asesoria', 'hora_asesoria','nombre_cliente', 'rut_cliente','tipo_asesoria', 'problemas_encontrados', 'asistentes']
        widgets = {
            "fecha_asesoria": forms.SelectDateWidget(),
            "hora_asesoria": forms.TimeInput(),
        }

class Asignar_asesoriaForm(ModelForm):
    class Meta:
        model = Asignar_asesoria
        fields = ['Solicitar_asesoria', 'Usuario', 'Profesional', 'gestion_accidentes', 'mejoras_propuestas', 'info_evento', 'diligencias_asociadas', 'juicios_asociados','estado_asesoria']
    

class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ['Visita', 'area_evaluada', 'uso_epi', 'señales_extintores', 'señales_no_fumar','entrenamiento_admision', 'validez_extintores', 'instalaciones_electricas',
        'instalaciones_sanitarias', 'alarmas_incendios', 'estado_herramientas', 'estado_materiales', 'resultado_visita', 'actividades', 'problemas_encontrados']



class ContratoForm(ModelForm):
    class Meta:
        model = Contrato
        fields = ['Usuario','fecha_inicio', 'fecha_termino', 'visitas_mes', 'asesorias_mes','capacitaciones_mes']
        widgets = {
            "fecha_inicio": forms.SelectDateWidget(),
            "fecha_termino": forms.SelectDateWidget(),
        }