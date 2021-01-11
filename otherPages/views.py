from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactEmailForm
from django.views.generic import TemplateView, FormView



class HomePageView(TemplateView):
    template_name = 'homePage.html'


class AboutPageView(TemplateView):
	template_name = 'aboutPage.html'


class BudgetPageView(TemplateView):
	template_name = 'budgetPage.html'


class ContactPageView(FormView):
    template_name = 'contactPage.html'
    form_class = ContactEmailForm

    def form_valid(self, form):
        email_message = ('<b>Email:</b> '+form.cleaned_data.get('from_email')+
                        '<br /><br />'+
                        '<b>Mensagem:</b> <br /><br />'+form.cleaned_data.get('email_message'))
        send_mail(
            'CONTATO SITE',
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            settings.DEFAULT_TO_EMAIL,
            fail_silently=True,
            html_message=email_message
        )
        
        return super().form_valid(form)

    def get_success_url(self, **kwargs):  
        messages.add_message(self.request, messages.INFO, "Mensagem enviada com sucesso!")
        return reverse('contact')
