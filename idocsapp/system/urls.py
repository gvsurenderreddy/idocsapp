from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.system.views import dashboard, hotelariadocs, postodocs, restodocs, institucionaldocs, calendar, agendar, profile, \
    desbravador41_31

urlpatterns = [

    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^perfil/', profile, name='profile'),
    url(r'^hotelariadocs/$', hotelariadocs, name="hotelariadocs"),
    url(r'^postodocs/$', postodocs, name="postodocs"),
    url(r'^restodocs/$', restodocs, name="restodocs"),
    url(r'^institucionaldocs/$', institucionaldocs, name="institucionaldocs"),
    url(r'^calendar/', calendar, name='calendar'),
    url(r'^agendar/', agendar, name='agendar'),
    url(r'^desbravador41_31/', desbravador41_31, name='desbravador41_31'),
    # url(r'^rol/', rol, name='rol'),

]
