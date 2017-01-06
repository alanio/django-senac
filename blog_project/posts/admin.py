from django.contrib import admin
from .models import Post, Categoria

class PostAdmin(admin.ModelAdmin):
    exclude = ('autor',)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'obs')

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
