from django.shortcuts import render
from .models import Sobre

def sobre(request):
    sobre = Sobre.objects.all()
    return render(request, 'sobre/index.html', {'sobre': sobre})