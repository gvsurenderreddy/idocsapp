from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.system.views import dashboard, hotelariadocs, postodocs, restodocs, institucionaldocs, calendar, profile

urlpatterns = [

    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^perfil/', profile, name='profile'),
    url(r'^hotelariadocs/$', hotelariadocs, name="hotelariadocs"),
    url(r'^postodocs/$', postodocs, name="postodocs"),
    url(r'^restodocs/$', restodocs, name="restodocs"),
    url(r'^institucionaldocs/$', institucionaldocs, name="institucionaldocs"),
    url(r'^calendar/', calendar, name='calendar'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
