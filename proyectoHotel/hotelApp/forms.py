from django import forms

class formulario_cliente(forms.Form):
    cliente_nombre = forms.CharField()
    cliente_apellido = forms.CharField()
    cliente_email = forms.EmailField()

class formulario_empleado(forms.Form):
    empleado_nombre = forms.CharField()
    empleado_apellido = forms.CharField()
    empleado_area = forms.CharField()
    
class formulario_habitacion(forms.Form):
    habitacion_tipo = forms.CharField()
    habitacion_fecha_reserva = forms.DateField()
    habitacion_numero = forms.IntegerField()