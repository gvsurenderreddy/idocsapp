# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import RegisterForm


def register(resquest):
    template_name = 'register.html'
    if resquest.method == 'POST':
        form = RegisterForm(resquest.POST, resquest.FILES)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(resquest, template_name, context)


def login(request):
    return render(request, 'login.html')


def lockscreen(request):
    return render(request, 'lockscreen.html')
