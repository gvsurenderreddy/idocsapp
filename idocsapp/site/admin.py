from django import forms
from django.contrib import admin

from idocsapp.site.models import Contact, Documents


class ContactsForm(forms.ModelForm):
    class Media:
        css = {
            'all': ('static/css/geoposition_override.css',)
        }
        js = ('static/js/geoposition_override.js',)


class ContactsAdmin(admin.ModelAdmin):
    form = ContactsForm
    list_display = (
        'contact_name', 'contact_img', 'contact_slug', 'contact_email', 'contact_tel', 'contact_city', 'contact_state',
        'contact_created_at')
    list_filter = ['contact_sex']
    search_fields = ['contact_name', 'contact_email', 'contact_address', 'contact_city']
    save_on_top = True
    prepopulated_fields = {'contact_slug': ('contact_name',)}


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('documents_name', 'documents_slug', 'documents_birth_date')
    list_filter = ['documents_name']
    search_fields = ['documents_name', 'documents_slug']
    save_on_top = True
    prepopulated_fields = {'documents_slug': ('documents_name',)}


admin.site.register(Contact, ContactsAdmin)
admin.site.register(Documents, DocumentsAdmin)
