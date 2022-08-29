from django.urls import path
from AppIntermedia.views import *


urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('supervisor/', supervisor, name="supervisor"),
    path('empleado/', empleado, name="empleado"),
    path('usuario/', usuario, name="usuario"),
    path('supervisorformulario/', supervisorFormulario, name="supervisorformulario"),
    path('empleadoformulario/', empleadoFormulario, name="empleadoformulario"),
    path('usuarioformulario/', usuarioFormulario, name="usuarioformulario"),
    path('busquedanumero/', busquedaNumero, name="busquedanumero"),
    path('resultadobusqueda/', busqueda, name="resultadobusqueda"),




]