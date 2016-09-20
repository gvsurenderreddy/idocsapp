# -*- coding: utf-8 -*-
from django.db import models
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.utils import timezone
from geoposition.fields import GeopositionField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.br_states import STATE_CHOICES


class Documents(models.Model):
    DOCUMENTS_TYPE_CHOICE = (

        ('desbravador 41_31', 'Desbravador 41_31'),
        ('light 3', 'Light 3'),
        ('desbravador Easy special', 'Desbravador Easy special'),
        ('light', 'Light'),
        ('light Web', 'Light Web'),
        ('rol', 'ROL'),
        ('ipdv', 'IPDV'),
        ('gas', 'Gas'),
        ('fast', 'Fast'),

    )

    DOCUMENTS_MODULE_TYPE_CHOICE = (

        ('gerência hoteleira', 'Gerência Hoteleira'),
        ('financeiro', 'Financeiro'),
        ('estoque', 'Estoque'),
        ('tarifador', 'Tarifador'),
        ('PDVA', 'PDVA'),
        ('contábil', 'Contábil'),
        ('CRM_Fidelidade', 'CRM_Fidelidade'),
        ('rol', 'ROL'),
        ('fiscal', 'Fiscal'),
        ('eventos', 'Eventos'),
        ('condomínio', 'Condomínio'),
        ('gas', 'Gas'),
        ('Fast', 'Fast'),

    )


    documents_type = models.CharField('Sistema', max_length=100, choices=DOCUMENTS_TYPE_CHOICE)
    documents_module_type = models.CharField('Módulo', max_length=100, choices=DOCUMENTS_MODULE_TYPE_CHOICE)
    documents_name = models.CharField('Nome', max_length=100)
    documents_subject = models.CharField('Assunto', max_length=100)
    documents_slug = models.SlugField('Atalho')
    documents_description = models.TextField('Descrição')  # blank=true significa que nao e obrigatorio
    documents_birth_date = models.DateField('Data de origem', null=True, blank=True)
    documents_img = models.ImageField(upload_to='imagens', verbose_name='Imagem', blank=True)
    documents_archive = models.FileField(upload_to='Documentos', verbose_name='Arquivo', blank=True)
    documents_created_at = models.DateTimeField('Criado em', auto_now_add=True)  # auto now vai pegar a data atual
    documents_updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.documents_name


    @models.permalink
    def get_absolute_url(self):
        return ('site:index.html', (), {'documents_slug': self.course_slug})

    class Meta:
        verbose_name = 'Documentos'
        verbose_name_plural = 'Documentos'
        ordering = ['documents_name']

class Agendar(models.Model):
    CONTACT_UTIL_CHOICE = (

        ('colaborador', 'Colaborador'),
        ('cliente', 'Cliente'),
        ('fornecedor', 'Fornecedor'),
        ('prestador de servico', 'Prestador de servico'),
        ('lógica', 'Lógica'),

    )

    contact_name = models.CharField('Name', max_length=100)
    contact_slug = models.SlugField('Atalho')
    contact_type = models.CharField('Grupo', max_length=100, choices=CONTACT_UTIL_CHOICE, blank=True)
    contact_email = models.EmailField('E-mail',max_length=100, blank=True)
    contact_ddd = models.IntegerField('DDD', blank=True)
    contact_main_number = models.IntegerField('Principal')
    contact_fix_number = models.IntegerField('Fixo', blank=True, null=True)
    contact_cellphone_number = models.IntegerField('Celular', blank=True, null=True)
    contact_notes = models.TextField('Obs', max_length=200, blank=True)
    contact_date_created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.contact_name

    @models.permalink
    def get_absolute_url(self):
        return ('site:agendar.html', (), {'contact_slug': self.course_slug})

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agenda'
        ordering = ['contact_name']
