from django.contrib import admin
from .models import *

#Ingresar modelos para manejar desde el panel de admin.

admin.site.register(Consolas)
admin.site.register(Juegos)
admin.site.register(Perifericos)
admin.site.register(Avatar)
admin.site.register(Comentarios)
