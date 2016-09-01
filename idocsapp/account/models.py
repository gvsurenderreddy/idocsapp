# -*- coding: utf-8 -*-
import re

from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('O nome de usuário dado deve ser ajustado'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Login'), max_length=15, unique=True,
                                help_text=_('Requeridos 15 caracteres ou menos. so pode conter Letras, \
                    nnmeros e @/./+/-/_'),
                                validators=[
                                    validators.RegexValidator(
                                        re.compile('^[\w.@+-]+$'),
                                        _('Entre com um nome de usuario valido'),
                                        _('invalido'))])
    first_name = models.CharField(_('Primeiro nome'), max_length=30)
    last_name = models.CharField(_('Ultimo nome'), max_length=30)
    email = models.EmailField(_('E-mail'), max_length=255, unique=True)
    end = models.EmailField(_('Endereco'), max_length=255)
    city = models.EmailField(_('Cidade'), max_length=255)
    state = models.EmailField(_('Estado'), max_length=255)
    tel = models.IntegerField(_('Telefone'), max_length=255)
    funcion = models.CharField(_('Cargo'), max_length=30)
    is_staff = models.BooleanField(_('E da equipe'), default=False,
                                   help_text=_('Designa se o usuario pode registrar neste local do admin.'))
    is_active = models.BooleanField(_('Ativo'), default=True,
                                    help_text=_('Designa se este usuario deve ser tratado como ativo. \
                    desmarque isto em vez de suprimir clientes.'))
    date_joined = models.DateTimeField(_('Data de inicio'), default=timezone.now)
    is_trusty = models.BooleanField(_('E confiavel'), default=False,
                                    help_text=_('Designa se este usuario confirmou seu email.'))
    avatar = models.ImageField('Foto para perfil', upload_to='imagens/avatar', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = UserManager()

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def _unicode_(self):
        return self.username
