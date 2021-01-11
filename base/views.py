from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class MobileMenuView(TemplateView):
	template_name = 'mobile_menu.html'
