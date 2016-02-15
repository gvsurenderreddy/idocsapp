# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.br_states import STATE_CHOICES


class Documents(models.Model):
    DOCUMENTS_TYPE_CHOICE = (

        ('desbravador41_31', 'Desbravador41_31'),
        ('desbravador Light3', 'Desbravador Light3'),
        ('desbravador Easy special', 'Desbravador Easy special'),
        ('rol', 'ROL'),

    )

    documents_type = models.CharField('Tipo do documento', max_length=100, choices=DOCUMENTS_TYPE_CHOICE)
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
        return ('site:teste.html', (), {'documents_slug': self.course_slug})

    class Meta:
        verbose_name = 'Documentos'
        verbose_name_plural = 'Documentos'
        ordering = ['documents_name']
