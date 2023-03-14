from django.urls import path
from hotelApp import views

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('habitaciones', views.vista_renderHTML_habitacion,name='Habitaciones'),
    path('empleados', views.vista_renderHTML_empleado,name = 'Empleados'),
    path('cliente',views.cliente,name='Cliente'),
    path('buscar_clientes', views.vista_renderHTML_buscar_cliente),
    path('vista_resultado_busqueda',views.vista_resultado_busqueda),
    path('vista_formulario_cliente', views.vista_formulario_cliente),
    path('vista_formulario_habitacion', views.vista_formulario_habitacion),
    path('vista_formulario_empleado', views.vista_formulario_empleado),
    path('resultado_busqueda_clientes',views.vista_resultado_busqueda),
]