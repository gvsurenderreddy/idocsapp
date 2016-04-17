from django.contrib import admin

from idocsapp.system.models import Documents, Agendar


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('documents_name', 'documents_slug', 'documents_birth_date')
    list_filter = ['documents_name']
    search_fields = ['documents_name', 'documents_slug']
    save_on_top = True
    prepopulated_fields = {'documents_slug': ('documents_name',)}


class AgendarAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_slug', 'contact_main_number', 'contact_date_created_at')
    list_filter = ['contact_name']
    search_fields = ['contact_name', 'documents_slug']
    save_on_top = True
    prepopulated_fields = {'contact_slug': ('contact_name',)}


admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Agendar, AgendarAdmin)