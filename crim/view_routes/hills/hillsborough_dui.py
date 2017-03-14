
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *
from crim.models import search_all

def hillsborough_dui(request):
    hillsb_judge = HillsboroughJudges(request)

    if request.method == 'POST':
        print("Hello")
        hillsb_judge = HillsboroughJudges(request.POST)


        if hillsb_judge.is_valid():
            judge = hillsb_judge.cleaned_data['hillsb_judge']
            print(judge)
            if judge == 'farr':
                return render(request, 'crim/fl/hills/dui/farr-dui.html')
            elif judge == 'greco':
                return render(request, 'crim/fl/hills/dui/greco-dui.html')
            elif judge == 'jeske':
                return render(request, 'crim/fl/hills/dui/jeske-dui.html')
            elif judge == 'lefler':
                return render(request, 'crim/fl/hills/dui/lefler-dui.html')
            elif judge == 'mcneil':
                return render(request, 'crim/fl/hills/dui/mcneil-dui.html')
            elif judge == 'myers':
                return render(request, 'crim/fl/hills/dui/myers-dui.html')
            elif judge == 'taylor':
                return render(request, 'crim/fl/hills/dui/taylor-dui.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/hills/dui/dui.html')

    else:
        hillsb_judge = HillsboroughJudges()

    return render(request, 'crim/fl/hills/hillsborough-dui.html', {'hillsb_judge': hillsb_judge})

def dui(request):
    return render(request, 'crim/fl/hills/dui/dui.html' )

def farr(request):
    return render(request, 'crim/fl/hills/dui/farr-dui.html')


def greco(request):
    return render(request, 'crim/fl/hills/dui/grecodui.html')

def lefler(request):
    return render(request, 'crim/fl/hills/dui/lefler-dui.html')

def jeske(request):
    return render(request, 'crim/fl/hills/dui/jeske-dui.html')

def mcneil(request):
    return render(request, 'crim/fl/hills/dui/mcneil-dui.html')

def myers(request):
    return render(request, 'crim/fl/hills/dui/myers-dui.html')

def taylor(request):
    return render(request, 'crim/fl/hills/dui/taylor-dui.html')
