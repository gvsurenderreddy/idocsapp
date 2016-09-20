# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20160215_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usu\xe1rio', 'verbose_name_plural': 'Usu\xe1rios'},
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.IntegerField(verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Requeridos 15 caracteres ou menos. so pode conter Letras,                     nnmeros e @/./+/-/_', unique=True, max_length=15, verbose_name='Login', validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), 'Entre com um nome de usuario valido', 'invalido')]),
        ),
    ]
