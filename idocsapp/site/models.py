# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from localflavor.br.forms import BRPhoneNumberField
from localflavor.br.br_states import STATE_CHOICES


class Contact(models.Model):
    SEX_CHOICES = (

        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    )

    MARITAL_STATUS_CHOICES = (

        ('solteiro', 'Solteiro'),
        ('divorciado', 'Divorciado'),
        ('casado', 'Casado'),
        ('viuvo', 'Viuvo'),

    )

    UF_CHOICES = (

        ('AC-Acre', 'AC-Acre'), ('AL-Alagoas', 'AL-Alagoas'), ('AP-Amapá', 'AP-Amapá'),
        ('AM-Amazonas', 'AM-Amazonas'),
        ('BA - Bahia', 'BA - Bahia'), ('CE - Ceará', 'CE - Ceará'), ('DF - Distrito Federal', 'DF - Distrito Federal'),
        ('ES - Espírito Santo', 'ES - Espírito Santo'), ('GO - Goiás', 'GO - Goiás'),
        ('MA - Maranhão', 'MA - Maranhão'),
        ('MT - Mato Grosso', 'MT - Mato Grosso'), ('MS - Mato Grosso do Sul', 'MS - Mato Grosso do Sul'),
        ('MG - Minas Gerais', 'MG - Minas Gerais'),
        ('PA - Pará', 'PA - Pará'), ('PB - Paraíba', 'PB - Paraíba'), ('PR - Paraná', 'PR - Paraná'),
        ('PE - Pernambuco', 'PE - Pernambuco'),
        ('PI - Piauí', 'PI - Piauí'), ('RJ - Rio de Janeiro', 'RJ - Rio de Janeiro'),
        ('RN - Rio Grande do Norte', 'RN - Rio Grande do Norte'),
        ('RS - Rio Grande do Sul', 'RS - Rio Grande do Sul'), ('RO - Rondônia', 'RO - Rondônia'),
        ('RR - Roraima', 'RR - Roraima'),
        ('SC - Santa Catarina', 'SC - Santa Catarina'),
        ('SP - São Paulo', 'SP - São Paulo'), ('SE - Sergipe', 'SE - Sergipe'), ('TO - Tocantins', 'TO - Tocantins')

    )

    contact_img = models.ImageField('Foto do Contato', upload_to='imagens', blank=True, null=True)
    contact_name = models.CharField('Nome', max_length=100)
    contact_slug = models.SlugField('Atalho')
    contact_tel = models.IntegerField('Telefone')
    contact_email = models.EmailField('E-mail', max_length=100)
    contact_birth = models.DateField('Data de Nascimento')
    contact_sex = models.CharField('Sexo', max_length=50, choices=SEX_CHOICES)
    contact_marital_satus = models.CharField('Estado Civil', max_length=50, choices=MARITAL_STATUS_CHOICES)
    contact_favorite = models.BooleanField('Favorito')
    contact_address = models.CharField('Endereço', max_length=255,
                                       help_text='Para uma melhor localização no mapa, preencha sem abreviações. Ex: Rua Martinho Estrela,  1229')
    contact_neighborhood = models.CharField('Bairro', max_length=255)
    contact_city = models.CharField('Cidade', max_length=255,
                                    help_text='Para uma melhor localização no mapa, preencha sem abreviações. Ex: Belo Horizonte')
    contact_state = models.CharField('Estado', max_length=20, choices=STATE_CHOICES)
    contact_position = GeopositionField('localização',
                                        help_text='Não altere os valores calculados automaticamente de latitude e longitude')
    contact_description = models.TextField('Descrição')
    contact_created_at = models.DateTimeField('Criado em', auto_now_add=True)  # auto now vai pegar a data atual
    contact_updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['contact_name']
