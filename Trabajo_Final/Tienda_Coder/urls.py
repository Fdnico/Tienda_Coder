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
    path('Tienda_Coder/periferico_ver/', Ver_Periferico, name='periferico_ver'),
    path('Tienda_Coder/periferico_crear/', Crear_Periferico, name='periferico_crear'),
    path('Tienda_Coder/periferico_borrar/', Borrar_Periferico, name='periferico_borrar'),
    path('Tienda_Coder/periferico_editar/', Editar_Periferico, name='periferico_editar'),
    path('Tienda_Coder/periferico_buscar/', Buscar_Periferico, name='periferico_buscar'),
    path('Tienda_Coder/periferico_resultado_buscar/', Resultado_Buscar_Periferico, name='periferico_resultado_buscar'),

    path('Tienda_Coder/consolas/', Vista_Consolas, name='consolas'),
    path('Tienda_Coder/consola_ver/', Ver_Consola, name='consola_ver'),
    path('Tienda_Coder/consola_crear/', Crear_Consola, name='consola_crear'),
    path('Tienda_Coder/consola_borrar/', Borrar_Consola, name='consola_borrar'),
    path('Tienda_Coder/consola_editar/', Editar_Consola, name='consola_editar'),
    path('Tienda_Coder/consola_buscar/', Buscar_Consola, name='consola_buscar'),
    path('Tienda_Coder/consola_resultado_buscar/', Resultado_Buscar_Consola, name='consola_resultado_buscar'),

    path('Tienda_Coder/juegos/', Vista_Juegos, name='juegos'),
    path('Tienda_Coder/juego_ver/', Ver_Juego, name='juego_ver'),
    path('Tienda_Coder/juego_crear/', Crear_Juego, name='juego_crear'),
    path('Tienda_Coder/juego_borrar/', Borrar_Juego, name='juego_borrar'),
    path('Tienda_Coder/juego_editar/', Editar_Juego, name='juego_editar'),
    path('Tienda_Coder/juego_buscar/', Buscar_Juego, name='juego_buscar'),
    path('Tienda_Coder/juego_resultado_buscar/', Resultado_Buscar_Juego, name='juego_resultado_buscar'),
    ]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)