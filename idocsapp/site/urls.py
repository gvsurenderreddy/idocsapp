from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.site.views import index, proposal, company, contacts, download, teste

urlpatterns = [

    url(r'^$', index, name='index'),
    url(r'^proposta/$', proposal, name='proposal'),
    url(r'^empresa/$', company, name='company'),
    url(r'^download/$', download, name='download'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^teste/$', teste, name='teste'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
