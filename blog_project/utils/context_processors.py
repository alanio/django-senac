# usando context processors do django
from blog_project.posts.models import Categoria

def lista_categorias(request):
    return {
        'lista_categorias': Categoria.objects.all()
    }