from django import forms

class FormularioSupervisor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    ano_nacimiento = forms.IntegerField()


class FormularioEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    ano_nacimiento = forms.IntegerField()


class FormularioUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    ano_nacimiento = forms.IntegerField()