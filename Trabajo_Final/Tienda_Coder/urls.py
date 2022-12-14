from django.contrib import admin
from django.urls import path
from Tienda_Coder.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('Tienda_Coder/inicio/', index, name='inicio'),

    path('Tienda_Coder/login/', Iniciar_Sesion, name='auth_login'),
    path('Tienda_Coder/register/', Registrar_Usuario, name='registrar_usuario'),
    path('Tienda_Coder/logout/', LogoutView.as_view(template_name='Tienda_Coder/logout.html'), name='auth_logout'),
    
    path('Tienda_Coder/editar_perfil/', Editar_Perfil, name='auth-perfil-editar'),
    path('Tienda_Coder/agregar_avatar/', Agregar_Avatar, name='auth-avatar'),

    path('Tienda_Coder/perifericos/', Vista_Perifericos, name='perifericos'),
    path('Tienda_Coder/ver_periferico/', Ver_Periferico, name='ver_periferico'),
    path('Tienda_Coder/crear_periferico/', Crear_Periferico, name='crear_periferico'),
    path('Tienda_Coder/borrar_periferico/', Borrar_Periferico, name='borrar_periferico'),
    path('Tienda_Coder/editar_periferico/', Editar_Periferico, name='editar_periferico'),
    path('Tienda_Coder/buscar_periferico/', Buscar_Periferico, name='buscar_periferico'),
    path('Tienda_Coder/resultado_buscar_periferico/', Resultado_Buscar_Periferico, name='resultado_buscar_periferico'),

    path('Tienda_Coder/consolas/', Vista_Consolas, name='consolas'),
    path('Tienda_Coder/ver_consola/', Ver_Consola, name='ver_consola'),
    path('Tienda_Coder/crear_consola/', Crear_Consola, name='crear_consola'),
    path('Tienda_Coder/borrar_consola/', Borrar_Consola, name='borrar_consola'),
    path('Tienda_Coder/editar_consola/', Editar_Consola, name='editar_consola'),
    path('Tienda_Coder/buscar_consola/', Buscar_Consola, name='buscar_consola'),
    path('Tienda_Coder/resultado_buscar_consola/', Resultado_Buscar_Consola, name='resultado_buscar_consola'),

    path('Tienda_Coder/juegos/', Vista_Juegos, name='juegos'),
    path('Tienda_Coder/ver_juego/', Ver_Juego, name='ver_juego'),
    path('Tienda_Coder/crear_juego/', Crear_Juego, name='crear_juego'),
    path('Tienda_Coder/borrar_juego/', Borrar_Juego, name='borrar_juego'),
    path('Tienda_Coder/editar_juego/', Editar_Juego, name='editar_juego'),
    path('Tienda_Coder/buscar_juego/', Buscar_Juego, name='buscar_juego'),
    path('Tienda_Coder/resultado_buscar_juego/', Resultado_Buscar_Juego, name='resultado_buscar_juego'),
]
