# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_img', models.ImageField(upload_to=b'imagens', null=True, verbose_name=b'Foto do Contato', blank=True)),
                ('contact_name', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('contact_slug', models.SlugField(verbose_name=b'Atalho')),
                ('contact_tel', models.IntegerField(verbose_name=b'Telefone')),
                ('contact_email', models.EmailField(max_length=100, verbose_name=b'E-mail')),
                ('contact_birth', models.DateField(verbose_name=b'Data de Nascimento')),
                ('contact_sex', models.CharField(max_length=50, verbose_name=b'Sexo', choices=[(b'masculino', b'Masculino'), (b'feminino', b'Feminino')])),
                ('contact_marital_satus', models.CharField(max_length=50, verbose_name=b'Estado Civil', choices=[(b'solteiro', b'Solteiro'), (b'divorciado', b'Divorciado'), (b'casado', b'Casado'), (b'viuvo', b'Viuvo')])),
                ('contact_favorite', models.BooleanField(verbose_name=b'Favorito')),
                ('contact_address', models.CharField(help_text=b'Para uma melhor localiza\xc3\xa7\xc3\xa3o no mapa, preencha sem abrevia\xc3\xa7\xc3\xb5es. Ex: Rua Martinho Estrela,  1229', max_length=255, verbose_name=b'Endere\xc3\xa7o')),
                ('contact_neighborhood', models.CharField(max_length=255, verbose_name=b'Bairro')),
                ('contact_city', models.CharField(help_text=b'Para uma melhor localiza\xc3\xa7\xc3\xa3o no mapa, preencha sem abrevia\xc3\xa7\xc3\xb5es. Ex: Belo Horizonte', max_length=255, verbose_name=b'Cidade')),
                ('contact_state', models.CharField(max_length=20, verbose_name=b'Estado', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('contact_position', geoposition.fields.GeopositionField(help_text=b'N\xc3\xa3o altere os valores calculados automaticamente de latitude e longitude', max_length=42, verbose_name=b'localiza\xc3\xa7\xc3\xa3o')),
                ('contact_description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('contact_created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('contact_updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Atualizado em')),
            ],
            options={
                'ordering': ['contact_name'],
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documents_name', models.CharField(max_length=100, verbose_name=b'Nome')),
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
