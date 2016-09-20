# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from idocsapp.system.models import Documents, Agendar


@login_required
def dashboard(request):
    return render(request, 'system/dashboard.html')


@login_required
def hotelariadocs(request):
    return render(request, 'system/hotelaria/hotelariadocs.html')


@login_required
def postodocs(request):
    return render(request, 'system/postos/postodocs.html')


@login_required
def restodocs(request):
    return render(request, 'system/restaurantes/restodocs.html')


@login_required
def institucionaldocs(request):
    return render(request, 'system/institucional/institucionaldocs.html')


@login_required
def calendar(request):
    return render(request, 'system/institucional/calendar.html')


@login_required
def waitlist(request):
    return render(request, 'system/institucional/waitlist.html')


@login_required
def errosgerais(request):
    return render(request, 'system/institucional/errosgerais.html')


@login_required
def agendar(request):
    list_agendar = Agendar.objects.order_by('contact_name')
    return render(request, 'system/institucional/agendar.html', {'list_agendar': list_agendar})


@login_required
def profile(request):
    return render(request, 'system/profile.html')


@login_required
def desbravador41_31(request):
    return render(request, 'system/hotelaria/41/desbravador41_31.html')


@login_required
def desbravador41_31GerenciaHoteleiraDocs(request):
    list_documents = Documents.objects.order_by('documents_name')
    return render(request, 'system/hotelaria/41/gerenciaHoteleiraDocs.html', {'list_documents': list_documents})


@login_required
def desbravadorLight3(request):
    return render(request, 'system/hotelaria/light3/desbravadorLight3.html')


@login_required
def desbravadorLight3Docs(request):
    list_documents = Documents.objects.order_by('documents_name')
    return render(request, 'system/hotelaria/light3/desbravadorLight3Docs.html', {'list_documents': list_documents})
