from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib import admin
from django.conf import settings
# Create your models here. 


class Usuario(AbstractUser):
    rut = models.CharField('Rut', max_length=100, blank=False, null=True)
    nombre_empresa = models.CharField('Nombre Empresa', max_length=100, blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=100, blank=False, null=True)
    telefono = models.CharField('Telefono', max_length=40, blank=True, null=True)
    rubro = models.CharField('Rubro', max_length=40, blank=True, null=True)

    def __str__(self):
         return f"{self.username},{self.first_name},{self.last_name},{self.nombre_empresa}, {self.rut}, {self.rubro}"

class Profesional(models.Model):
    nombre_prof = models.CharField('Nombre Profesional', max_length=100, blank=True, null=True)
    apellido_prof = models.CharField('Apellido Profesional', max_length=100, blank=True, null=True)
    correo_prof = models.CharField('Correo Profesional', max_length=100, blank=True, null=True)
    telefono_prof = models.CharField('Telefono Profesional', max_length=100, blank=True, null=True)

    def __str__(self):
         return f"{self.nombre_prof}, {self.apellido_prof},{self.correo_prof}"


class Capacitacion(models.Model):
    fecha_capacitacion = models.DateField(verbose_name="Fecha Capacitacion")
    hora_capacitacion = models.TimeField(verbose_name="Hora Capacitacion")
    asistentes_capacitacion = models.IntegerField(blank=False, null=False, verbose_name="Asistentes")
    materiales_capacitacion = models.CharField(max_length=100, blank=False, null=False, verbose_name="Materiales")
    capacitacion_extra = models.BooleanField(verbose_name="Es capacitacion extra")
    monto_capacitacion = models.CharField(max_length=45, blank=False, null=False, verbose_name="Valor Capacitacion")
    fecha_termino_capacitacion = models.DateField(verbose_name="Fecha Termino Capacitacion")
    hora_termino_capacitacion = models.TimeField(verbose_name="Hora Termino Capacitacion")
    Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    Profesional = models.OneToOneField(Profesional, on_delete=models.CASCADE)
   

class Visita(models.Model):
    fecha_inicio = models.DateField(verbose_name="Fecha Inicio")
    fecha_termino = models.DateField(verbose_name="Fecha Termino")
    hora_inicio = models.TimeField(verbose_name="Hora Inicio")
    hora_termino = models.TimeField(verbose_name="Hora Termino")
    visita_extra = models.BooleanField(verbose_name="Es visita extra")
    Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    Profesional = models.OneToOneField(Profesional, on_delete=models.CASCADE)
    

    def __str__(self):
         return f"{self.fecha_inicio}, {self.fecha_termino},{self.hora_inicio},{self.hora_termino},{self.Usuario}, {self.Profesional}"

class Checklist(models.Model):
    Visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
    area_evaluada = models.CharField(max_length=45, blank=False, null=False, verbose_name="Area Evaluada")
    uso_epi = models.BooleanField(verbose_name="Uso de Equipos de Proteccion")
    señales_extintores = models.BooleanField(verbose_name="Señales de Extintores")
    señales_no_fumar = models.BooleanField(verbose_name="Señales de No Fumar")
    entrenamiento_admision = models.BooleanField(verbose_name="Entrenamiento del personal")
    validez_extintores = models.BooleanField(verbose_name="Validez extintores")
    instalaciones_electricas = models.BooleanField(verbose_name="Instalaciones electricas")
    instalaciones_sanitarias = models.BooleanField(verbose_name="Instalaciones sanitarias")
    alarmas_incendios = models.BooleanField(verbose_name="Alarmas contra Incendio")
    estado_herramientas= models.BooleanField(verbose_name="Herramientas")
    estado_materiales = models.BooleanField(verbose_name="Materiales")
    resultado_visita = models.CharField(max_length=100, blank=False, null=False, verbose_name="Resultado Visita")
    actividades = models.CharField(max_length=45, blank=False, null=False, verbose_name="Actividades Necesarias")
    problemas_encontrados = models.CharField(max_length=45, blank=False, null=False, verbose_name="Problemas de Seguridad encontrados")

    def __str__(self):
         return f"{self.Visita}, {self.area_evaluada},{self.uso_epi},{self.resultado_visita},{self.actividades}, {self.problemas_encontrados}"

class Solicitar_asesoria(models.Model):
    fecha_asesoria = models.DateField(verbose_name="Fecha Asesoria")
    hora_asesoria = models.TimeField(verbose_name="Hora Asesoria")
    nombre_cliente = models.CharField(max_length=45, blank=False, null=False, verbose_name="Nombre Cliente")
    rut_cliente = models.CharField(max_length=45, blank=False, null=False, verbose_name="Rut Cliente")
    tipo_asesoria = models.CharField(max_length=45, blank=False, null=False, verbose_name="Tipo de Asesoria")
    problemas_encontrados = models.CharField(max_length=45, blank=False, null=False, verbose_name="Problemas Encontrados")
    asistentes = models.IntegerField(blank=False, null=False, verbose_name="Asistentes Involucrados")

    def __str__(self):
         return f"{self.fecha_asesoria},{self.nombre_cliente},{self.rut_cliente},{self.tipo_asesoria}"


class Asignar_asesoria(models.Model):
    Solicitar_asesoria = models.ForeignKey(Solicitar_asesoria, on_delete=models.CASCADE)
    Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    Profesional = models.OneToOneField(Profesional, on_delete=models.CASCADE)
    gestion_accidentes = models.CharField(max_length=45, blank=False, null=False, verbose_name="Gestion Accidentes")
    mejoras_propuestas = models.CharField(max_length=45, blank=False, null=False, verbose_name="Mejoras Propuestas")
    info_evento = models.CharField(max_length=45, blank=False, null=False, verbose_name="Informacion del Evento")
    diligencias_asociadas = models.CharField(max_length=45, blank=False, null=False, verbose_name="Diligencias Asociadas")
    juicios_asociados = models.CharField(max_length=45, blank=False, null=False, verbose_name="Juicios Asociados")
    estado_asesoria = models.BooleanField(verbose_name="Asesoria Completada")

class Contrato(models.Model):
    Usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(verbose_name="Fecha Inicio")
    fecha_termino = models.DateField(verbose_name="Fecha Termino")
    visitas_mes = models.CharField(max_length=45, blank=False, null=False, verbose_name="Visitas por mes")
    asesorias_mes = models.CharField(max_length=45, blank=False, null=False, verbose_name="Asesorias por mes")
    capacitaciones_mes = models.CharField(max_length=45, blank=False, null=False, verbose_name="Capacitaciones por mes")
