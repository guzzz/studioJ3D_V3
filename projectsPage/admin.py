
from .models import Project
from django.contrib import admin
from django.utils.safestring import mark_safe

from .services import resize_image


class ProjectAdmin(admin.ModelAdmin):
	fieldsets = (
        ('Informações do Projeto', {
            'fields': (
                'description', 'space' ,'position', 'photo', 'small_photo'
            ),
        }),
    )
	list_display = ( 'thumbnail', 'position', 'create_at' )
	search_fields = ['position']
	list_filter = ['space']


	def thumbnail(self, obj):
		if obj.id:
			return mark_safe('<image src="%s" height="200" width="200"/>' % obj.small_photo.url)
		return ''
admin.site.register(Project, ProjectAdmin)
