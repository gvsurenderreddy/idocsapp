# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20160131_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='end',
            field=models.EmailField(default=1, max_length=255, verbose_name='Endereco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='tel',
            field=models.IntegerField(default=1, max_length=255, verbose_name='Telefone'),
            preserve_default=False,
        ),
    ]
