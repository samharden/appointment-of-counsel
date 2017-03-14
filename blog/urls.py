from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/should-first-time-dui-offenders-have-ignition-interlock.html',
            views.ignition_interlock, name='ignition-interlock'),
    url(r'^posts/florida-stand-your-ground.html',
        views.stand_your_ground, name='stand-your-ground'),
    url(r'^posts/the-defendant-and-the-algorithm',
        views.defendant_and_algorithm, name='defendant-and-algorithm'),
    ]
