from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import modelo_cliente,modelo_empleado,modelo_habitacion
from .forms import formulario_cliente,formulario_empleado,formulario_habitacion

# Create your views here.
def vista_renderHTML_cliente(request):
    return render(request, 'clientes.html')

def vista_renderHTML_habitacion(request):
    return render(request, 'habitaciones.html')

def vista_renderHTML_empleado(request):
    return render(request, 'empleados.html')

def vista_busquedaHTML_cliente(request):
    return render(request, 'busquedaPaciente.html')

def vista_buscarHTML(request):
    if request.GET['nombre']:
        cliente_nombre=request.GET['cliente_nombre']
        clientes= modelo_cliente.objects.filter(cliente_nombre__icontains=cliente_nombre)
        context={'clientes':clientes}
        return render(request,'resultado.html',context)
    else:
        return HttpResponse("No se encontró ningun cliente con esos datos")

def vista_formulario_cliente(request):
    if request.method=='POST':
        formulario = formulario_cliente(request.POST)
        print(formulario)
        if formulario.is_valid():
            form_data = formulario.cleaned_data
            cliente = modelo_cliente(cliente_nombre=form_data['cliente_nombre'],cliente_apellido=form_data['cliente_apellido'],cliente_email=form_data['cliente_email'])
            cliente.save()
            return render(request,'inicio.html')
        else:
            formulario=formulario_habitacion()
    return render(request, "formulario_cliente.html")

def vista_formulario_empleado(request):
    if request.method=='POST':
        formulario=formulario_empleado(request.POST)
        print(formulario)
        if formulario.is_valid():
            form_data=formulario.cleaned_data
            empleado = modelo_empleado(empleado_nombre=form_data['empleado_nombre'],empleado_apellido=form_data['empleado_apellido'],empleado_legajo=form_data['empleado_legajo'])
            empleado.save()
            return render(request,'inicio.html')
        else:
            formulario=formulario_habitacion()
    return render(request, "formularioDoctor.html")

def vista_formulario_habitacion(request):
    if request.method=='POST':
        formulario=formulario_habitacion(request.POST)
        print(formulario)
        if formulario.is_valid():
            form_data=formulario.cleaned_data
            habitacion = modelo_habitacion(habitacion_tipo=form_data['habitacion_tipo'],fecha_reserva=form_data['fecha_reserva'],habitacion_numero=form_data['habitacion_numero'])
            habitacion.save()
            return render(request,'inicio.html')
        else:
            formulario=formulario_habitacion()
    return render(request, "formularioTurno.html",)
