from django.contrib import admin
from .models import Sobre

class SobreAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(Sobre, SobreAdmin)