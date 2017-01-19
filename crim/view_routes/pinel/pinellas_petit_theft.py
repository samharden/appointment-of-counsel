
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def pinellas_petit_theft(request):
    pinell_judge = PinellasJudges(request)
    crim_desc = CrimDesc(request)
    print("Pinellas petit-theft Page")
    if request.method == 'POST':
        print("Hello")
        pinell_judge = PinellasJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if pinell_judge.is_valid():
            print("Valid Hello there")
            judge = pinell_judge.cleaned_data['pinell_judge']
            print(judge)
            if judge == 'bedinghaus':
                return render(request, 'crim/fl/pinellas/petit-theft/bedinghaus.html')
            elif judge == 'carballo':
                return render(request, 'crim/fl/pinellas/petit-theft/carballo.html')
            elif judge == 'dittmer':
                return render(request, 'crim/fl/pinellas/petit-theft/dittmer.html')
            elif judge == 'horrox':
                return render(request, 'crim/fl/pinellas/petit-theft/horrox.html')
            elif judge == 'levine':
                return render(request, 'crim/fl/pinellas/petit-theft/levine.html')
            elif judge == 'mckyton':
                return render(request, 'crim/fl/pinellas/petit-theft/mckyton.html')
            elif judge == 'overton':
                return render(request, 'crim/fl/pinellas/petit-theft/overton.html')
            elif judge == 'pierce':
                return render(request, 'crim/fl/pinellas/petit-theft/pierce.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/pinellas/petit-theft/petit-theft.html')

    else:
        pinell_judge = PinellasJudges()

    return render(request, 'crim/fl/pinellas/petit-theft.html', {'pinell_judge': pinell_judge})

def petit_theft(request):
    return render(request, 'crim/fl/pinellas/petit-theft/petit-theft.html')

def bedinghaus(request):
    return render(request, 'crim/fl/pinellas/petit-theft/bedinghaus.html')

def carballo(request):
    return render(request, 'crim/fl/pinellas/petit-theft/carballo.html')

def dittmer(request):
    return render(request, 'crim/fl/pinellas/petit-theft/dittmer.html')

def horrox(request):
    return render(request, 'crim/fl/pinellas/petit-theft/horrox.html')

def levine(request):
    return render(request, 'crim/fl/pinellas/petit-theft/levine.html')

def mckyton(request):
    return render(request, 'crim/fl/pinellas/petit-theft/mckyton.html')

def overton(request):
    return render(request, 'crim/fl/pinellas/petit-theft/overton.html')

def pierce(request):
    return render(request, 'crim/fl/pinellas/petit-theft/pierce.html')
