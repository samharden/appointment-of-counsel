
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def pinellas_battery(request):
    pinell_judge = PinellasJudges(request)
    crim_desc = CrimDesc(request)
    print("Pinellas battery Page")
    if request.method == 'POST':
        print("Hello")
        pinell_judge = PinellasJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if pinell_judge.is_valid():
            print("Valid Hello there")
            judge = pinell_judge.cleaned_data['pinell_judge']
            print(judge)
            if judge == 'bedinghaus':
                return render(request, 'crim/fl/pinellas/battery/bedinghaus.html')
            elif judge == 'carballo':
                return render(request, 'crim/fl/pinellas/battery/carballo.html')
            elif judge == 'dittmer':
                return render(request, 'crim/fl/pinellas/battery/dittmer.html')
            elif judge == 'horrox':
                return render(request, 'crim/fl/pinellas/battery/horrox.html')
            elif judge == 'levine':
                return render(request, 'crim/fl/pinellas/battery/levine.html')
            elif judge == 'mckyton':
                return render(request, 'crim/fl/pinellas/battery/mckyton.html')
            elif judge == 'overton':
                return render(request, 'crim/fl/pinellas/battery/overton.html')
            elif judge == 'pierce':
                return render(request, 'crim/fl/pinellas/battery/pierce.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/pinellas/battery/battery.html')

    else:
        pinell_judge = PinellasJudges()

    return render(request, 'crim/fl/pinellas/battery.html', {'pinell_judge': pinell_judge})

def battery(request):
    return render(request, 'crim/fl/pinellas/battery/battery.html')

def bedinghaus(request):
    return render(request, 'crim/fl/pinellas/battery/bedinghaus.html')

def carballo(request):
    return render(request, 'crim/fl/pinellas/battery/carballo.html')

def dittmer(request):
    return render(request, 'crim/fl/pinellas/battery/dittmer.html')

def horrox(request):
    return render(request, 'crim/fl/pinellas/battery/horrox.html')

def levine(request):
    return render(request, 'crim/fl/pinellas/battery/levine.html')

def mckyton(request):
    return render(request, 'crim/fl/pinellas/battery/mckyton.html')

def overton(request):
    return render(request, 'crim/fl/pinellas/battery/overton.html')

def pierce(request):
    return render(request, 'crim/fl/pinellas/battery/pierce.html')
