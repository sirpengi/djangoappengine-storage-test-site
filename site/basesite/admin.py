from django.contrib import admin

from .models import (
	File,
)


class FileAdmin(admin.ModelAdmin):
	
	fields = [ 'get_absolute_url', 'title', 'admin_image' ]
	readonly_fields = [ 'get_absolute_url', 'admin_image', 'thumbnail' ]
	list_display = [ 'title', 'get_absolute_url', 'thumbnail' ]

admin.site.register(File, FileAdmin)
