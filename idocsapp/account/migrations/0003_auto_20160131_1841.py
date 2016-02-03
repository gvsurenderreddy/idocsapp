# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160130_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=b'imagens/avatar', null=True, verbose_name=b'Foto para perfil', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Requeridos 15 caracteres ou menos. so pode conter Letras,                     nnmeros e @/./+/-/_', unique=True, max_length=15, verbose_name='Usuario', validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), 'Entre com um nome de usuario valido', 'invalido')]),
        ),
    ]
