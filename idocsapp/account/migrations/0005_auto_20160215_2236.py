# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160215_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.EmailField(default=1, max_length=255, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.EmailField(default=1, max_length=255, verbose_name='Estado'),
            preserve_default=False,
        ),
    ]
