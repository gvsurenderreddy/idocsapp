# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20160918_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='documents_type',
            field=models.CharField(max_length=100, verbose_name=b'Sistema', choices=[(b'desbravador 41_31', b'Desbravador 41_31'), (b'light 3', b'Light 3'), (b'desbravador Easy special', b'Desbravador Easy special'), (b'light', b'Light'), (b'light Web', b'Light Web'), (b'rol', b'ROL'), (b'ipdv', b'IPDV'), (b'gas', b'Gas'), (b'fast', b'Fast')]),
        ),
    ]
