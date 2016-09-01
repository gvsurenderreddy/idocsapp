# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_documents_documents_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('contact_slug', models.SlugField(verbose_name=b'Atalho')),
                ('contact_type', models.CharField(max_length=100, verbose_name=b'Grupo', choices=[(b'colaborador', b'Colaborador'), (b'cliente', b'Cliente'), (b'fornecedor', b'Fornecedor'), (b'prestador de servi\xc3\xa7o', b'Prestador de servi\xc3\xa7o')])),
                ('contact_email', models.EmailField(max_length=100, verbose_name=b'E-mail')),
                ('contact_ddd', models.IntegerField(verbose_name=b'DDD')),
                ('contact_main_number', models.IntegerField(verbose_name=b'Principal')),
                ('contact_fix_number', models.IntegerField(verbose_name=b'Fixo')),
                ('contact_celphone_number', models.IntegerField(verbose_name=b'Celular')),
                ('contact_notes', models.TextField(max_length=200, verbose_name=b'Notes')),
                ('contact_date_created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
            ],
            options={
                'ordering': ['contact_name'],
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agenda',
            },
        ),
    ]
