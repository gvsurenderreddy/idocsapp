"""iDocsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from idocsapp.site import views
from idocsapp.account import views
from idocsapp.system import views

urlpatterns = [

    url(r'^', include('idocsapp.site.urls', namespace='site')),
    url(r'^', include('idocsapp.account.urls', namespace='account')),
    url(r'^', include('idocsapp.system.urls', namespace='system')),
    url(r'^admin/', include(admin.site.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
