# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='user',
            name='funcion',
            field=models.CharField(default=1, max_length=30, verbose_name='Cargo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de inicio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Primeiro nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designa se este usuario deve ser tratado como ativo.                     desmarque isto em vez de suprimir clientes.', verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designa se o usuario pode registrar neste local do admin.', verbose_name='E da equipe'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_trusty',
            field=models.BooleanField(default=False, help_text='Designa se este usuario confirmou seu email.', verbose_name='E confiavel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Ultimo nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Requeridos 15 caracteres ou menos. Letras,                     nnmeros and @/./+/-/_', unique=True, max_length=15, verbose_name='Usuario', validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), 'Entre com um nome de usuario valido', 'invalido')]),
        ),
    ]
