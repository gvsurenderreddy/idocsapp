# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documents_name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('documents_subject', models.CharField(max_length=100, verbose_name=b'Assunto')),
                ('documents_slug', models.SlugField(verbose_name=b'Atalho')),
                ('documents_description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('documents_birth_date', models.DateField(null=True, verbose_name=b'Data de origem', blank=True)),
                ('documents_img', models.ImageField(upload_to=b'imagens', verbose_name=b'Imagem', blank=True)),
                ('documents_archive', models.FileField(upload_to=b'Documentos', verbose_name=b'Arquivo', blank=True)),
                ('documents_created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('documents_updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Atualizado em')),
            ],
            options={
                'ordering': ['documents_name'],
                'verbose_name': 'Documentos',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
