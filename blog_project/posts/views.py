from django.shortcuts import render, get_object_or_404

from .models import Post

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post.html', {'post': post})

def lista_posts_categoria(request, id_categoria):
    posts_categoria = Post.objects.filter(categoria=id_categoria)
    return render(request, 'posts/lista_posts_categoria.html', {'posts_categoria':posts_categoria})