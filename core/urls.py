from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import registrar_usuario, mantenedor_usuario, detalle_usuario,crear_usuario,editar_usuario,eliminar_usuario,mantenedor_profesional,crear_profesional,editar_profesional,eliminar_profesional, control_asesoria, crear_checklist,editar_checklist,eliminar_checklist, mantenedor_checklist,registro, index, mantenedor_asesoria, editar_asesoria, eliminar_asesoria, responder_asesoria, planificar_visita,listar_visita,editar_visita, eliminar_visita, servicios, login, crear_capacitacion, listar_capacitacion, editar_capacitacion, eliminar_capacitacion, solicitar_asesoria, mantenedor_asesoria, detalle_asesoria, editar_asesoria2, eliminar_asesoria2, registrar_contrato, mantenedor_contrato, editar_contrato, eliminar_contrato
#usuariocreate

app_name = 'aseguradoraNMA'

urlpatterns = [
    path('', index, name="index"),
    #path('registrar_cliente/',registrar_cliente, name="registrar_cliente"),#ADMINISTRADOR Y PROFESIONAL
    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/index.html'), name ="logout"),
    path('registro/',registro, name="registro"),
    path('registrar_usuario', registrar_usuario, name="registrar_usuario"),#ADMINISTRADOR
    path('mantenedor_usuario/', views.mantenedor_usuario, name = 'mantenedor_usuario'), #PROFESIONAL
    path('detalle_usuario_<int:id>/', views.detalle_usuario, name = 'detalle_usuario'), #PROFESIONAL
    #path('detalle_cliente_<int:id>/', views.detalle_cliente, name = 'detalle_cliente'), #PROFESIONAL
    path('crear_usuario/', views.crear_usuario , name = 'crear_usuario'), #PROFESIONAL
    path('editar_usuario_<int:id>/' , views.editar_usuario , name = 'editar_usuario'), #PROFESIONAL
    path('eliminar_usuario_<int:id>/' , views.eliminar_usuario , name = 'eliminar_usuario'), #PROFESIONAL
    path('mantenedor_profesional/', views.mantenedor_profesional, name = 'mantenedor_profesional'), #PROFESIONAL
    path('crear_profesional/', views.crear_profesional , name = 'crear_profesional'), #PROFESIONAL
    path('editar_profesional_<int:id>/' , views.editar_profesional , name = 'editar_profesional'), #PROFESIONAL
    path('eliminar_profesional_<int:id>/' , views.eliminar_profesional , name = 'eliminar_profesional'), #PROFESIONAL
    path('servicios/', servicios, name="servicios"), #SERVICIOS
    path('crear_capacitacion/', crear_capacitacion, name="crear_capacitacion"),
    path('listar_capacitacion/', listar_capacitacion, name="listar_capacitacion"),
    path('editar_capacitacion/<id>/', editar_capacitacion, name="editar_capacitacion"),
    path('eliminar_capacitacion/<id>/', eliminar_capacitacion, name="eliminar_capacitacion"),
    path('planificar_visita/', planificar_visita, name="planificar_visita"),
    path('mantenedor_visita/', listar_visita, name="mantenedor_visita"),
    path('editar_visita/<id>/', editar_visita, name="editar_visita"),
    path('eliminar_visita/<id>/', eliminar_visita, name="eliminar_visita"),
    path('solicitar_asesoria/', solicitar_asesoria, name="solicitar_asesoria"),
    path('mantenedor_asesoria/', mantenedor_asesoria, name="mantenedor_asesoria"),
    path('editar_asesoria/<id>/', editar_asesoria, name="editar_asesoria"),
    path('detalle_asesoria/<id>/', detalle_asesoria, name="detalle_asesoria"),
    path('eliminar_asesoria/<id>/', eliminar_asesoria, name="eliminar_asesoria"),
    path('responder_asesoria/', responder_asesoria, name="responder_asesoria"),
    path('asesorias_respondidas/', control_asesoria, name="asesorias_respondidas"),
    path('editar_asesoria2/<id>/', editar_asesoria2, name="editar_asesoria2"),
    path('eliminar_asesoria2/<id>/', eliminar_asesoria2, name="eliminar_asesoria2"),
    path('mi_informacion/', control_asesoria, name="mi_informacion"),
    path('mantenedor_profesional/', views.mantenedor_profesional, name = 'mantenedor_profesional'),
    path('crear_checklist/', crear_checklist, name="crear_checklist"),
    path('editar_checklist_<int:id>/' , views.editar_checklist , name = 'editar_checklist'), 
    path('eliminar_checklist_<int:id>/' , views.eliminar_checklist , name = 'eliminar_checklist'),
    path('mantenedor_checklist/', mantenedor_checklist, name="mantenedor_checklist"),
    path('registrar_contrato/', registrar_contrato, name="registrar_contrato"),
    path('mantenedor_contrato/', mantenedor_contrato, name="mantenedor_contrato"),
    path('editar_contrato/<id>/', editar_contrato, name="editar_contrato"),
    path('eliminar_contrato/<id>/', eliminar_contrato, name="eliminar_contrato"),
]




