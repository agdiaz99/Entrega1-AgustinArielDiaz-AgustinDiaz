from django.urls import path
from AppIntermedia.views import *


urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('supervisor/', supervisor, name="supervisor"),
    path('empleado/', empleado, name="empleado"),
    path('usuario/', usuario, name="usuario"),
    path('supervisorFormulario/', supervisorFormulario, name="supervisorFormulario"),
    path('empleadoFormulario/', empleadoFormulario, name="empleadoFormulario"),
    path('usuarioFormulario/', usuarioFormulario, name="usuarioFormulario"),
    path('busquedaNombre/', busquedaNombre, name="busquedaNombre"),
    path('buscarEmpleado/', buscarEmpleado, name="buscarEmpleado"),
]