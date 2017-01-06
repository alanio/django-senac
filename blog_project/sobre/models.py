from django.db import models
from redactor.fields import RedactorField

class Sobre(models.Model):
    titulo = models.CharField(u'Título', max_length=100)
    descricao = RedactorField(u'Descrição') #models.TextField(u'Descricao')

    class Meta:
        verbose_name='Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return self.titulo

