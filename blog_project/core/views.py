from django.shortcuts import render
from blog_project.posts.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', {'posts': posts})