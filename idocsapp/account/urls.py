from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.account.views import register, login, lockscreen

urlpatterns = [

    url(r'^cadastro/', register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^bloqueio/', lockscreen, name='lockscreen'),
    url(r'^sair/', 'django.contrib.auth.views.logout', {'next_page': 'site:index'}, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
