from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    ordering = ['group', 'subject']
    list_display = ('id', 'title', 'group', 'subject', 'get_miniphoto', 'is_published')
    list_display_links = ('title', 'id')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_update', 'group', 'subject')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'description', 'group', 'subject', 'photo', 'get_miniphoto', 'pdf_file', 'time_create',
              'time_update', 'is_published',)
    readonly_fields = ('time_create', 'time_update', 'get_miniphoto')
    list_per_pag = 10

    def get_miniphoto(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_miniphoto.short_description = 'Обкладинка'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    list_display_links = ('id', 'number')
    search_fields = ('number',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Book, BookAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Subject, SubjectAdmin)
