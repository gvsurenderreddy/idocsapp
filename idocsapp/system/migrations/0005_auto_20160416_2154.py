# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20160416_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendar',
            name='contact_celphone_number',
            field=models.IntegerField(verbose_name=b'Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_ddd',
            field=models.IntegerField(verbose_name=b'DDD', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_email',
            field=models.EmailField(max_length=100, verbose_name=b'E-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_fix_number',
            field=models.IntegerField(verbose_name=b'Fixo', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_type',
            field=models.CharField(max_length=100, verbose_name=b'Grupo', choices=[(b'colaborador', b'Colaborador'), (b'cliente', b'Cliente'), (b'fornecedor', b'Fornecedor'), (b'prestador de servi\xc3\xa7o', b'Prestador de servi\xc3\xa7o'), (b'l\xc3\xb3gica', b'Logica')]),
        ),
    ]
