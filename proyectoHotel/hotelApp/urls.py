from django.urls import path
from hotelApp import views

urlpatterns = [
    path('vista_inicio/',views.inicio),
    path('vista_renderHTML-_clientes/', views.clientes, name="cliente"),
    path('vista_render_habitacion/', views.habitacion, name="habitacion"),
    path('vista_render_empleados/', views.empleado, name="empleado"),
    path('vista_cliente/', views.formulario_cliente, name="Formulario_cliente"),
    path('vista_habitacion/', views.formulario_habitacion, name="Formulario_habitacion"),
    path('vista_empleado/', views.formulario_empleado, name="Formulario_empleado"),
    path('vlista_busqueda_cliente/', views.busqueda_cliente, name="Busqueda_cliente"),
    path('vistabuscar/',views.buscar),
]