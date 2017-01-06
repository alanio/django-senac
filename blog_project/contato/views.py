from django.shortcuts import render
from .forms import ContatoForm

def contato(request):
    form = ContatoForm
    return render(request, 'contato/contato.html', {'form':form})