from django.db import models

class Contato(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    descricao = models.TextField(u'Descricao')

    def __str__(self):
        return self.titulo