from django.urls import path
from hotelApp import views

urlpatterns = [
    path('vista_inicio/',views.inicio),
    path('clientes/', views.vista_renderHTML_cliente, name="cliente"),
    path('habitaciones/', views.vista_renderHTML_habitacion, name="habitacion"),
    path('empleados/', views.vista_renderHTML_empleado, name="empleado"),
    path('buscar_clientes/', views.vista_busquedaHTML_cliente, name="Busqueda_cliente"),
    path('buscar/',views.vista_buscarHTML),
    path('formulario_cliente/', views.vista_formulario_cliente, name="formulario_cliente"),
    path('formulario_habitacion/', views.vista_formulario_habitacion, name="formulario_habitacion"),
    path('formulario_empleado/', views.vista_formulario_empleado, name="formulario_empleado"),
]