# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import ProposalForm, ContactsForm


def index(request):
    return render(request, 'index.html')


def company(request):
    return render(request, 'company.html')


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactsForm(request.POST, request.FILES)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = ContactsForm()
    else:
        form = ContactsForm()
    context['form'] = form
    template_name = 'contacts.html'
    return render(request, template_name, context)


def proposal(request):
    context = {}
    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = ProposalForm()
    else:
        form = ProposalForm()
    context['form'] = form
    template_name = 'proposal.html'
    return render(request, template_name, context)


def download(request):
    return render(request, 'download.html')


############TESTE Template##################################

def teste(request):
    return render(request, 'teste.html')
