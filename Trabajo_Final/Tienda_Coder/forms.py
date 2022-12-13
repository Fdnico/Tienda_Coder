from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.db import models

class Perifericos_Form(forms.Form):
    nombre = forms.CharField()
    marca = forms.CharField()
    precio = forms.IntegerField()


class Consolas_Form(forms.Form):
    nombre = forms.CharField()
    marca = forms.CharField()
    precio = forms.IntegerField()


class Juegos_Form(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null='True', blank='True')

#class Carrito_Form(forms.Form):
#    nombre = forms.CharField()
#    codigo_articulo = forms.IntegerField()
#    cantidad = forms.IntegerField()
#    precio = forms.IntegerField()