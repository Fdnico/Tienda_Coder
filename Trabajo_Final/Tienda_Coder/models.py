from django.db import models
from django.contrib.auth.models import User



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
