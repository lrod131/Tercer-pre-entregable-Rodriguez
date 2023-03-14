# Tercer-pre-entregable-Rodriguez

Django Hotel
Django Hotel es una aplicación web que permite a los usuarios reservar habitaciones de hotel, buscar clientes y empleados, y agregar nuevos clientes, empleados y habitaciones.

Requisitos
Para poder ejecutar esta aplicación, es necesario tener instalado lo siguiente:

->Python 3
->Django

Cómo ejecutar la aplicación:
1.- Clonar el repositorio:
https://github.com/lrod131/Tercer-pre-entregable-Rodriguez.git

2.- Ingresar al directorio de la aplicación:
cd django-hotel

3.- Crear un entorno virtual:
python3 -m venv venv

4.-Activar el entorno virtual:
source venv/bin/activate

5.- Crear las migraciones:
python manage.py makemigrations

6.- Aplicar las migraciones:
python manage.py migrate

7.-Iniciar la aplicación:
python manage.py runserver

8.-Acceder a la aplicación en el navegador, en la dirección http://localhost:8000/.

##Cómo utilizar la aplicación
La aplicación tiene las siguientes funcionalidades:

->Reservar habitaciones de hotel
->Buscar clientes
->Agregar nuevos clientes, empleados y habitaciones

Para reservar una habitación, basta con seleccionar la habitación deseada y la fecha de reserva.

Para buscar clientes, basta con ingresar el nombre del cliente en el formulario de búsqueda.

Para agregar un nuevo cliente, empleado o habitación, basta con ingresar la información correspondiente en el formulario de registro.

##Desarrollo
La aplicación está desarrollada en Django, utilizando el lenguaje de programación Python.

##Estructura del proyecto
hotel/: contiene las configuraciones generales del proyecto.
app/: contiene la lógica de la aplicación.
templates/: contiene las plantillas HTML de la aplicación.
static/: contiene los archivos estáticos de la aplicación (CSS, JS, etc.).

Archivos importantes
views.py: contiene las funciones que definen las vistas de la aplicación.
models.py: contiene las definiciones de los modelos de la aplicación.
forms.py: contiene las definiciones de los formularios de la aplicación.


Autor:
Luis Rodriguez
alexrod0890@gmail.com