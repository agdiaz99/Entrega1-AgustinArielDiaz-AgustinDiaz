from django.contrib import admin
from .models import Supervisor, Empleado, Usuario

# Register your models here.

admin.site.register(Supervisor)

admin.site.register(Empleado)

admin.site.register(Usuario)