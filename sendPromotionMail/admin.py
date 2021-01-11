
from .models import SendPromotionMail
from django.contrib import admin


class SendPromotionMailAdmin(admin.ModelAdmin):
	readonly_fields= ('sent', )
	fieldsets = (
	    ('Lista de e-mails enviados', {
	        'fields': (
	            'emails',
	        ),
	    }),
	)
	list_display = ( 'emails', 'sent' )
	search_fields = ['emails']

admin.site.register(SendPromotionMail, SendPromotionMailAdmin)