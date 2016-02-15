from django.contrib import admin

from idocsapp.system.models import Documents


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('documents_name', 'documents_slug', 'documents_birth_date')
    list_filter = ['documents_name']
    search_fields = ['documents_name', 'documents_slug']
    save_on_top = True
    prepopulated_fields = {'documents_slug': ('documents_name',)}


admin.site.register(Documents, DocumentsAdmin)
