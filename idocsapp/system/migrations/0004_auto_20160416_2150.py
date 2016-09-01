# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_agendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendar',
            name='contact_type',
            field=models.CharField(max_length=100, verbose_name=b'Grupo', choices=[(b'colaborador', b'Colaborador'), (b'cliente', b'Cliente'), (b'fornecedor', b'Fornecedor'), (b'prestador de servi\xc3\xa7o', b'Prestador de servi\xc3\xa7o'), (b'l\xc3\xb3gica', b'L\xc3\xb3gica')]),
        ),
    ]
