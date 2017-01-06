from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from redactor.fields import RedactorField
from django.utils.timezone import now 
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField(u'Titulo', max_length=100)
    conteudo = RedactorField(u'Descrição')
    #data_post = models.DateTimeField(auto_now_add=True)
    data_post = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(
        u"Publicação", default=now,
        help_text=u"A postagem será exibida somente após essa data.")
    autor = models.ForeignKey(User)
    tags = models.CharField(u'Tags', max_length=30)
    categoria = models.ForeignKey('Categoria')
    slug = AutoSlugField(populate_from='titulo')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']

class Categoria(models.Model):
    nome = models.CharField(u'Categoria', max_length=100)
    obs = models.TextField(u'Observação', blank=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.nome