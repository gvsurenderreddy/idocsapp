# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='documents_type',
            field=models.CharField(default=1, max_length=100, verbose_name=b'Tipo do documento', choices=[(b'desbravador41_31', b'Desbravador41_31'), (b'desbravador Light3', b'Desbravador Light3'), (b'desbravador Easy special', b'Desbravador Easy special'), (b'rol', b'ROL')]),
            preserve_default=False,
        ),
    ]
