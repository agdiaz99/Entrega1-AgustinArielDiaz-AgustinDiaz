from ast import For
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Supervisor, Empleado, Usuario
from AppIntermedia.forms import FormularioUsuario, FormularioEmpleado, FormularioSupervisor

# Create your views here.


def inicio(request):
    return render(request, "AppIntermedia/padre.html")

def supervisor(request):
    return render(request, "AppIntermedia/supervisor.html")

def usuario(request):
    return render(request, "AppIntermedia/usuario.html")

def empleado(request):
    return render(request, "AppIntermedia/empleado.html")

def supervisorFormulario(request):

    if request.method=="POST":
        miformulario= FormularioSupervisor(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            edad=info.get("edad")
            ano_nacimiento=info.get("ano_nacimiento")
            supervisor=Supervisor(nombre=nombre,apellido=apellido,edad=edad,ano_nacimiento=ano_nacimiento)
            supervisor.save()
            return render(request, "AppIntermedia/inicio.html", {"mensaje": "Supervisor creado"})
        else:
            return render(request, "AppIntermedia/supervisorFormulario.html", {"mensaje": "Error"})

    else:
        miformulario=FormularioSupervisor()
        return render(request, "AppIntermedia/supervisorFormulario.html", {"formulario":miformulario})



def empleadoFormulario(request):

    if request.method=="POST":
        miformulario= FormularioEmpleado(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            edad=info.get("edad")
            ano_nacimiento=info.get("ano_nacimiento")
            empleado=Empleado(nombre=nombre,apellido=apellido,edad=edad,ano_nacimiento=ano_nacimiento)
            empleado.save()
            return render(request, "AppIntermedia/inicio.html", {"mensaje":"Empleado creado"})
        else:
            return render(request, "AppIntermedia/empleadoFormulario.html", {"mensaje":"Error"})

    else:
        miformulario=FormularioEmpleado()
        return render(request, "AppIntermedia/empleadoFormulario.html", {"formulario":miformulario})
        

def usuarioFormulario(request):

    if request.method=="POST":
        miformulario= FormularioUsuario(request.POST)
        if miformulario.is_valid():
            info=miformulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            edad=info.get("edad")
            ano_nacimiento=info.get("ano_nacimiento")
            usuario=Usuario(nombre=nombre, apellido=apellido, edad=edad, ano_nacimiento=ano_nacimiento)
            usuario.save()
            return render(request, "AppIntermedia/inicio.html", {"mensaje": "Usuario creado"})
        else:
            return render(request, "AppIntermedia/inicio.html", {"mensaje": "Error"})

    else:
        miformulario=FormularioUsuario()
        return render(request, "AppIntermedia/usuarioFormulario.html", {"formulario":miformulario})

def busqueda(request):
    numero=request.GET["edad"]
    usuarios=Usuario.objects.filter(edad=numero)
    if len(usuarios)!=0:
        return render(request, "AppIntermedia/resultadoBusqueda.html", {"usuarios":usuarios})
    else:
        return render(request, "AppIntermedia/resultadoBusqueda.html", {"mensaje": "No hay resultados"})


def busquedaNumero(request):
    return render (request, "AppIntermedia/busquedaNumero.html")






        
        





            
            









