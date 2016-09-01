# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20160416_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendar',
            name='contact_notes',
            field=models.TextField(max_length=200, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_type',
            field=models.CharField(blank=True, max_length=100, verbose_name=b'Grupo', choices=[(b'colaborador', b'Colaborador'), (b'cliente', b'Cliente'), (b'fornecedor', b'Fornecedor'), (b'prestador de servico', b'Prestador de servico'), (b'logica', b'Logica')]),
        ),
    ]
