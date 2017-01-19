from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def hillsborough_battery(request):
    hillsb_judge = HillsboroughJudges(request)
    crim_desc = CrimDesc(request)
    print("Hillsborough Battery Page")
    if request.method == 'POST':
        print("Hello")
        hillsb_judge = HillsboroughJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if hillsb_judge.is_valid():
            print("Valid Hello there")
            judge = hillsb_judge.cleaned_data['hillsb_judge']
            print(judge)
            if judge == 'farr':
                
                return render(request, 'crim/fl/hills/battery/farrbattery.html')
            elif judge == 'greco':
                return render(request, 'crim/fl/hills/battery/grecobattery.html')
            elif judge == 'jeske':
                return render(request, 'crim/fl/hills/battery/jeskebattery.html')
            elif judge == 'lefler':
                return render(request, 'crim/fl/hills/battery/leflerbattery.html')
            elif judge == 'mcneil':
                return render(request, 'crim/fl/hills/battery/mcneilbattery.html')
            elif judge == 'myers':
                return render(request, 'crim/fl/hills/battery/myersbattery.html')
            elif judge == 'taylor':
                return render(request, 'crim/fl/hills/battery/taylorbattery.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/hills/battery/battery.html')

    else:
        hillsb_judge = HillsboroughJudges()

    return render(request, 'crim/fl/hills/hillsborough-battery.html', {'hillsb_judge': hillsb_judge})

def battery(request):
    return render(request, 'crim/fl/hills/battery/battery.html')

def farr(request):
    return render(request, 'crim/fl/hills/battery/farrbattery.html')

def greco(request):
    return render(request, 'crim/fl/hills/battery/grecobattery.html')

def lefler(request):
    return render(request, 'crim/fl/hills/battery/leflerbattery.html')

def jeske(request):
    return render(request, 'crim/fl/hills/battery/jeskebattery.html')

def mcneil(request):
    return render(request, 'crim/fl/hills/battery/mcneilbattery.html')

def myers(request):
    return render(request, 'crim/fl/hills/battery/myersbattery.html')

def taylor(request):
    return render(request, 'crim/fl/hills/battery/taylorbattery.html')
