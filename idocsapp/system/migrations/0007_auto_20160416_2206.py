# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20160416_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendar',
            name='contact_celphone_number',
        ),
        migrations.AddField(
            model_name='agendar',
            name='contact_cellphone_number',
            field=models.IntegerField(null=True, verbose_name=b'Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_fix_number',
            field=models.IntegerField(null=True, verbose_name=b'Fixo', blank=True),
        ),
    ]
