from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class SiteMap(sitemaps.Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            'home',
            'about',
            'disclaimer',
            'contact',



            'choose-complaint-type',
            'pub-acc-complaint',
            'housing-complaint',
            'employment-complaint',

            'complaint-choices',
            'sc-index',
            'complaint-choices-auto',
            'sc_complaint',
            'sc_complaint_auto',
            'sc_complaint_auto-md',

            ]


    def location(self, item):
        return reverse(item)
