"""mycourtcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from fl_discrim_helper import views
from blog import views
from main import views
from mycourtcase import sitemap
from mycourtcase.sitemap import SiteMap
from django.contrib.sitemaps.views import sitemap
from .sitemap import SiteMap

sitemaps = {
    'crim': SiteMap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^fl-discrim-helper/', include('fl_discrim_helper.urls')),
    url(r'^$', views.home_page, name='home'),
    url(r'^main/', include('main.urls')),
    url(r'^crim/', include('crim.urls')),
    url(r'^fl-mental-health/', include('mental_health.urls')),
    url(r'^fl-small-claims/', include('small_claims.urls')),
    url(r'^blog/', include('blog.urls')),
]
