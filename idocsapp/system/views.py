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
    return render(request, 'system/hotelariadocs.html')


@login_required
def postodocs(request):
    return render(request, 'system/postodocs.html')


@login_required
def restodocs(request):
    return render(request, 'system/restodocs.html')


@login_required
def institucionaldocs(request):
    return render(request, 'system/institucionaldocs.html')


@login_required
def calendar(request):
    return render(request, 'system/calendar.html')


@login_required
def agendar(request):
    list_agendar = Agendar.objects.order_by('contact_name')
    return render(request, 'system/agendar.html', {'list_agendar': list_agendar})


@login_required
def profile(request):
    return render(request, 'system/profile.html')


@login_required
def desbravador41_31(request):
    list_documents = Documents.objects.order_by('documents_name')
    return render(request, 'system/desbravador41_31.html', {'list_documents': list_documents})


# @login_required
# def rol(request):
#     list_documents = Documents.objects.order_by('documents_name')
#     return render(request, 'system/rol.html', {'list_documents': list_documents})
