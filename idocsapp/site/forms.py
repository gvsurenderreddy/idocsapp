# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

from idocsapp.site.mail import send_mail_template

MOBILEOPERATOR_CHOICES = (

    ('claro', 'CLARO'), ('nextel', 'NEXTEL'),
    ('oi', 'OI'), ('tim', 'TIM'),
    ('vivo', 'VIVO'),

)

STATE_CHOICES = (

    ('AC - Acre', 'AC - Acre'), ('AL - Alagoas', 'AL - Alagoas'), ('AP - Amapá', 'AP - Amapá'),
    ('AM Amazonas', 'AM - Amazonas'),
    ('BA - Bahia', 'BA - Bahia'), ('CE - Ceará', 'CE - Ceará'), ('DF - Distrito Federal', 'DF - Distrito Federal'),
    ('ES - Espírito Santo', 'ES - Espírito Santo'), ('GO - Goiás', 'GO - Goiás'), ('MA - Maranhão', 'MA - Maranhão'),
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

VESION_CHOICES = (

    ('Desbravador 4.1', 'Desbravador 4.1'), ('Desbravador 3.1', 'Desbravador 3.1'),
    ('Desbravador Light3', 'Desbravador Light3'),
    ('Desbravador Easy special', 'Desbravador Easy special'), ('Desbravador Light', 'Desbravador Light'),
    ('Desbravador Gas Station 10', 'Desbravador Gas Station 10'),
    ('Desbravador Gas Station ', 'Desbravador Gas Station'), ('Desbravador Liquor store', 'Desbravador Liquor store'),
    ('Desbravador Fast', 'Desbravador Fast'),
)


class ProposalForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'José da silva'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'contato@gmail.com'}))
    phone = forms.IntegerField(label='Telefone Fixo', required=False,
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '833445566'}))
    cellphone = forms.IntegerField(label='Celular', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '85999998877'}))
    mobileOperator = forms.ChoiceField(label='Operadora', widget=forms.Select, choices=MOBILEOPERATOR_CHOICES)
    whatsapp = forms.BooleanField(label='Tem Whatsapp?', initial=0, required=False, widget=forms.CheckboxInput)
    company = forms.CharField(label='Empresa', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Empresa Brasileira LTDA'}))
    site = forms.URLField(label='Site', max_length=80, required=False, widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'http://www.logicasuporte.com.br'}))
    city = forms.CharField(label='Cidade', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fortaleza'}))
    state = forms.ChoiceField(label='Estado', widget=forms.Select, choices=STATE_CHOICES)
    version = forms.ChoiceField(label='Versão preferida do sistema', widget=forms.Select, choices=VESION_CHOICES)
    attach = forms.FileField(label='Anexar arquivo', required=False, widget=forms.FileInput)
    obs = forms.CharField(label='Observações', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Media:
        css = {
            'all': ('style.css', 'bootstrap.min.css')
        }

    def send_mail(self):
        subject = 'Contato de proposta do site'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'cellphone': self.cleaned_data['cellphone'],
            'mobileOperator': self.cleaned_data['mobileOperator'],
            'whatsapp': self.cleaned_data['whatsapp'],
            'company': self.cleaned_data['company'],
            'site': self.cleaned_data['site'],
            'city': self.cleaned_data['city'],
            'state': self.cleaned_data['state'],
            'version': self.cleaned_data['version'],
            'attach': self.cleaned_data['attach'],
            'obs': self.cleaned_data['obs'],
        }

        template_name = 'proposal_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL],
                           from_email=settings.DEFAULT_FROM_EMAIL)


class ContactsForm(forms.Form):
    name = forms.CharField(label='Nome completo', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'José da silva'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'contato@gmail.com'}))
    phone = forms.IntegerField(label='Telefone',
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '833445566'}))
    attach = forms.FileField(label='Anexar arquivo', required=False, widget=forms.FileInput)
    msg = forms.CharField(label='Mensagem', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Media:
        css = {
            'all': ('style.css', 'bootstrap.min.css')
        }

    def send_mail(self):
        subject = 'Contato do site'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
            'attach': self.cleaned_data['attach'],
            'msg': self.cleaned_data['msg']

        }
        template_name = 'contacts_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL],
                           from_email=settings.DEFAULT_FROM_EMAIL)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
