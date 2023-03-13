from django.urls import path
from hotelApp import views

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('habitaciones', views.vista_renderHTML_habitacion,name='Habitaciones'),
    path('empleados', views.vista_renderHTML_empleado,name = 'Empleados'),
    path('buscar_clientes', views.vista_renderHTML_buscar_cliente),
    path('buscar',views.vista_resultado_busqueda),
    path('formulario_cliente', views.vista_formulario_cliente),
    path('formulario_habitacion', views.vista_formulario_habitacion),
    path('formulario_empleado', views.vista_formulario_empleado),
    path('test',views.cliente,name='Cliente'),
]