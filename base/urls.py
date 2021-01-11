
from django.conf.urls import url
from projectsPage.views import ProjectsPageView, TPageView
from otherPages.views import  AboutPageView, BudgetPageView, ContactPageView, HomePageView
from base.views import MobileMenuView


urlpatterns = [
	url(r'^$',HomePageView.as_view(), name='home'),
	url(r'^about/$', AboutPageView.as_view(), name='about'),
	url(r'^projects/$', ProjectsPageView.as_view(), name='projects'),
	url(r'^budget/$', BudgetPageView.as_view(), name='budget'),
	url(r'^contact/$',ContactPageView.as_view(), name='contact'),
	url(r'^mobile_menu/$',MobileMenuView.as_view(), name='mm'),
	url(r'^360/(?P<pk>[0-9]+)/$',TPageView.as_view(), name='360'),
]