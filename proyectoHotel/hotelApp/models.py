from django.db import models

class modelo_cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=30)
    cliente_apellido = models.CharField(max_length=30)
    cliente_email = models.EmailField()

class modelo_empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    empleado_nombre = models.CharField(max_length=30)
    empleado_apellido = models.CharField(max_length=30)
    empleado_area = models.CharField(max_length=30)
    
class modelo_habitacion(models.Model):
    habitacion_id = models.AutoField(primary_key=True)
    habitacion_tipo = models.CharField(max_length=30)
    habitacion_fecha_reserva = models.DateField()
    habitacion_numero = models.IntegerField()