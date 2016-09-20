from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.system.views import dashboard, hotelariadocs, postodocs, restodocs, institucionaldocs, calendar, agendar, errosgerais, profile, \
    desbravador41_31, desbravador41_31GerenciaHoteleiraDocs, desbravadorLight3, desbravadorLight3Docs, waitlist

urlpatterns = [

    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^perfil/', profile, name='profile'),
    url(r'^hotelariadocs/$', hotelariadocs, name="hotelariadocs"),
    url(r'^postodocs/$', postodocs, name="postodocs"),
    url(r'^restodocs/$', restodocs, name="restodocs"),
    url(r'^institucionaldocs/$', institucionaldocs, name="institucionaldocs"),
    url(r'^calendar/', calendar, name='calendar'),
    url(r'^waitlist/', waitlist, name='waitlist'),
    url(r'^agendar/', agendar, name='agendar'),
    url(r'^errosgerais/', errosgerais, name='errosgerais'),
    url(r'^desbravador41_31/', desbravador41_31, name='desbravador41_31'),
    url(r'^desbravador41_31GerenciaHoteleiraDocs/', desbravador41_31GerenciaHoteleiraDocs, name='desbravador41_31GerenciaHoteleiraDocs'),
    url(r'^desbravadorLight3/', desbravadorLight3, name='desbravadorLight3'),
    url(r'^desbravadorLight3Docs/', desbravadorLight3Docs, name='desbravadorLight3Docs'),

]
