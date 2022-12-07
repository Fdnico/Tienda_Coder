from django.db import models

#Modelos a usar

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

    def __str__(self):
        return self.nombre

# class Carrito(models.Model):
#     id = models.CharField()
#     cantidad = models.IntegerField()
#     suma_total = models.IntegerField()
