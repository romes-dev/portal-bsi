from django.contrib import admin
from .models import Image, Usuario

admin.site.register(Image)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    search_fields = ('nome', 'email')

admin.site.register(Usuario, UsuarioAdmin)