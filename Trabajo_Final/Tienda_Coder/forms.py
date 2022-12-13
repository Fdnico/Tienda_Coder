from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='User')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Correo Electronico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Correo Electronico')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirme el Password', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        help_texts = {'email': 'Indica un correo electronico que utilices habitualmente', 'first_name': '', 'last_name': '', 'password': ''}


class AvatarForm(forms.Form):
    imagen = forms.ImageField()
