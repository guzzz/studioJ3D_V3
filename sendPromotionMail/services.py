
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def get_emails_list(emails):
	
	if emails:
		return emails.split(";")


def send_single_mail(email):
	
	to = []
	to.append(email)

	msg_plain = render_to_string('promotionalMail/promotional-mail.txt')
	msg_html = render_to_string('promotionalMail/promotional-mail.html')

	from_email = settings.DEFAULT_FROM_EMAIL
	subject = 'STUDIO J3D - Imagens 3D com o melhor custo benefício do mercado!'

	response = send_mail(
		subject,
		msg_plain,
		from_email,
		to,
		fail_silently=False,
		html_message=msg_html 
	)
	if response == 1:
		return True
	else:
		return False