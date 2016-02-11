from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.account.views import register, login, lockscreen

urlpatterns = [

    url(r'^cadastro/', register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}, name='login'),
    url(r'^bloqueio/', lockscreen, name='lockscreen'),
    url(r'^sair/', 'django.contrib.auth.views.logout', {'next_page': 'site:index'}, name='logout'),

]
