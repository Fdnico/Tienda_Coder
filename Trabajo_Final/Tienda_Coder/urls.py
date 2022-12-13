from django.contrib import admin
from django.urls import path
from Tienda_Coder.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('tcoder/inicio/', index, name='inicio'),

    path('tcoder/login/', Iniciar_Sesion, name='auth_login'),
    path('tcoder/register/', Registrar_Usuario, name='registrar_usuario'),
    path('tcoder/logout/', LogoutView.as_view(template_name='tcoder/logout.html'), name='auth_logout'),
    
    path('tcoder/editar_perfil/', Editar_Perfil, name='auth-perfil-editar'),
    path('tcoder/agregar_avatar/', Agregar_Avatar, name='auth-avatar'),

    path('tcoder/perifericos/', Vista_Perifericos, name='perifericos'),
    path('tcoder/ver_periferico/', Ver_Periferico, name='ver_periferico'),
    path('tcoder/crear_periferico/', Crear_Periferico, name='crear_periferico'),
    path('tcoder/borrar_periferico/', Borrar_Periferico, name='borrar_periferico'),
    path('tcoder/editar_periferico/', Editar_Periferico, name='editar_periferico'),
    path('tcoder/buscar_periferico/', Buscar_Periferico, name='buscar_periferico'),
    path('tcoder/resultado_buscar_periferico/', Resultado_Buscar_Periferico, name='resultado_buscar_periferico'),

    path('tcoder/consolas/', Vista_Consolas, name='consolas'),
    path('tcoder/ver_consola/', Ver_Consola, name='ver_consola'),
    path('tcoder/crear_consola/', Crear_Consola, name='crear_consola'),
    path('tcoder/borrar_consola/', Borrar_Consola, name='borrar_consola'),
    path('tcoder/editar_consola/', Editar_Consola, name='editar_consola'),
    path('tcoder/buscar_consola/', Buscar_Consola, name='buscar_consola'),
    path('tcoder/resultado_buscar_consola/', Resultado_Buscar_Consola, name='resultado_buscar_consola'),

    path('tcoder/juegos/', Vista_Juegos, name='juegos'),
    path('tcoder/ver_juego/', Ver_Juego, name='ver_juego'),
    path('tcoder/crear_juego/', Crear_Juego, name='crear_juego'),
    path('tcoder/borrar_juego/', Borrar_Juego, name='borrar_juego'),
    path('tcoder/editar_juego/', Editar_Juego, name='editar_juego'),
    path('tcoder/buscar_juego/', Buscar_Juego, name='buscar_juego'),
    path('tcoder/resultado_buscar_juego/', Resultado_Buscar_Juego, name='resultado_buscar_juego'),
]
