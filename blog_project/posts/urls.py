from django.conf.urls import url

from . import views
 
urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.post, name= 'post'),
    url(r'categoria/(?P<id_categoria>[0-9]+)/$', views.lista_posts_categoria, name='lista_posts_categoria') ,
]