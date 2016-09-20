# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20160918_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendar',
            name='contact_notes',
            field=models.TextField(max_length=200, verbose_name=b'Obs', blank=True),
        ),
        migrations.AlterField(
            model_name='agendar',
            name='contact_type',
            field=models.CharField(blank=True, max_length=100, verbose_name=b'Grupo', choices=[(b'colaborador', b'Colaborador'), (b'cliente', b'Cliente'), (b'fornecedor', b'Fornecedor'), (b'prestador de servico', b'Prestador de servico'), (b'l\xc3\xb3gica', b'L\xc3\xb3gica')]),
        ),
        migrations.AlterField(
            model_name='documents',
            name='documents_module_type',
            field=models.CharField(max_length=100, verbose_name=b'M\xc3\xb3dulo', choices=[(b'ger\xc3\xaancia hoteleira', b'Ger\xc3\xaancia Hoteleira'), (b'financeiro', b'Financeiro'), (b'estoque', b'Estoque'), (b'tarifador', b'Tarifador'), (b'PDVA', b'PDVA'), (b'cont\xc3\xa1bil', b'Cont\xc3\xa1bil'), (b'CRM_Fidelidade', b'CRM_Fidelidade'), (b'rol', b'ROL'), (b'fiscal', b'Fiscal'), (b'eventos', b'Eventos'), (b'condom\xc3\xadnio', b'Condom\xc3\xadnio'), (b'gas', b'Gas'), (b'Fast', b'Fast')]),
        ),
        migrations.AlterField(
            model_name='documents',
            name='documents_type',
            field=models.CharField(max_length=100, verbose_name=b'Sistema', choices=[(b'desbravador41_31', b'Desbravador 41_31'), (b'light 3', b'Light 3'), (b'desbravador Easy special', b'Desbravador Easy special'), (b'light', b'Light'), (b'light Web', b'Light Web'), (b'rol', b'ROL'), (b'ipdv', b'IPDV'), (b'gas', b'Gas'), (b'fast', b'Fast')]),
        ),
    ]
