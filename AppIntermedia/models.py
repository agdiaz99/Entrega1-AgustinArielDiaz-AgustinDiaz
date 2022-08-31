from django.db import models

# Create your models here.


class Supervisor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    ano_nacimiento = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)


class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    ano_nacimiento = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    ano_nacimiento = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)