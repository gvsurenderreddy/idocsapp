# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20160918_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='documents_description',
            field=models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
        ),
    ]
