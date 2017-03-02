from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r'^$', auth_views.login, name='homepage'),
    url(r'^detail.html', views.search_page, name='search'),
    url(r'^about.html', views.about, name='about'),
    url(r'^disclaimer.html', views.disclaimer, name='disclaimer'),
    url(r'^contact.html', views.contact, name='contact'),

]



# urlpatterns = [
#     url(r'^$', views.home_page, name='homepage'),
#
# ]
