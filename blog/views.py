from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

def ignition_interlock(request):
    return render(request, 'posts/should-first-time-dui-offenders-have-ignition-interlock.html')
