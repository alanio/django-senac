
from django.conf.urls import url, include
from django.contrib import admin

#
from django.conf import settings
from django.conf.urls.static import static

from blog_project.core import urls as core_urls
from blog_project.sobre import urls as sobre_urls
from blog_project.contato import urls as contato_urls
from blog_project.posts import urls as posts_urls


urlpatterns = [
    url(r'', include(core_urls, namespace='core')),
    url(r'^sobre/', include(sobre_urls, namespace = 'sobre')), 
    url(r'^post/', include(posts_urls, namespace = 'posts')),
    url(r'^contato/', include(contato_urls, namespace = 'contato')), 
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', admin.site.urls),
  	#url(r'^categoria/', admin.site.urls),


] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ADMIN'
admin.site.index_title = 'BLOG DJANGO'
admin.site.site_title = 'Site de Administração'