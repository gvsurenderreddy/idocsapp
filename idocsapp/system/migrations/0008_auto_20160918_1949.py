# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20160416_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='documents_module_type',
            field=models.CharField(default=1, max_length=100, verbose_name=b'Modulo', choices=[(b'gerencia hoteleira', b'Gerencia Hoteleira'), (b'financeiro', b'Financeiro'), (b'estoque', b'Estoque'), (b'tarifador', b'Tarifador'), (b'PDVA', b'PDVA'), (b'contabil', b'Contabil'), (b'CRM Fidelidade', b'CRM fidelidade'), (b'rol', b'ROL'), (b'fiscal', b'Fiscal'), (b'eventos', b'Eventos'), (b'condominio', b'Condominio'), (b'gas', b'Gas'), (b'Fast', b'Fast')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documents',
            name='documents_description',
            field=models.TextField(verbose_name=b'Descricao'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='documents_type',
            field=models.CharField(max_length=100, verbose_name=b'Tipo do documento', choices=[(b'desbravador41_31', b'Desbravador41_31'), (b'light3', b'Light3'), (b'desbravador Easy special', b'Desbravador Easy special'), (b'light', b'Light'), (b'light Web', b'Light Web'), (b'rol', b'ROL'), (b'IPDV', b'IPDV'), (b'gas', b'Gas'), (b'fast', b'fast')]),
        ),
    ]
