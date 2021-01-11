
from django.db import models
from .services import *
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import send_mail


def custom_save(email):
	obj = SendPromotionMail()
	obj.emails = email
	try:
		obj.sent = send_single_mail(email)
		obj.tried = True
		obj.save()
	except:
		obj.sent = False
		obj.tried = True
		obj.save()


class SendPromotionMail(models.Model):
	emails = models.CharField(
        _('E-mail'), max_length=3000, blank=False, null=False, 
        help_text='Para enviar mais de um e-mail, separe os mesmos por ";"'
    )
	tried = models.BooleanField(_('Tentou enviar?'), default=False)
	sent = models.BooleanField(_('Enviado?'), default=False)


	class Meta:
		ordering = ['-sent','emails']
		verbose_name = _('uma tentiva de envio de e-mail')
		verbose_name_plural = _('Enviar e-mails de divulgação')

	def save(self, *args, **kwargs):
		emails_list = []
		emails_list = get_emails_list(self.emails)
		
		if emails_list:
			
			if len(emails_list) > 1:
				for email in emails_list:
					custom_save(email.strip())
			else:
				if not self.tried:
					custom_save(emails_list[0].strip())
				else:
					super(SendPromotionMail, self).save(*args, **kwargs)



	