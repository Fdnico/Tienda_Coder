from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Consolas(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre


class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre


class Perifericos(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='imagen_periferico', null='True', blank='True')

    def __str__(self):
        return self.nombre
    

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null='True', blank='True')

class Comentarios(models.Model):
    usuario = models.CharField(max_length=30)
    imagen = imagen = models.ImageField(upload_to='imagen_periferico', null='True', blank='True')
    comentario = models.CharField(max_length= 150)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario