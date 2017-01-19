
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def pinellas_dwlsr(request):
    pinell_judge = PinellasJudges(request)
    crim_desc = CrimDesc(request)
    print("Pinellas dwlsr Page")
    if request.method == 'POST':
        print("Hello")
        pinell_judge = PinellasJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if pinell_judge.is_valid():
            print("Valid Hello there")
            judge = pinell_judge.cleaned_data['pinell_judge']
            print(judge)
            if judge == 'bedinghaus':
                return render(request, 'crim/fl/pinellas/dwlsr/bedinghaus.html')
            elif judge == 'carballo':
                return render(request, 'crim/fl/pinellas/dwlsr/carballo.html')
            elif judge == 'dittmer':
                return render(request, 'crim/fl/pinellas/dwlsr/dittmer.html')
            elif judge == 'horrox':
                return render(request, 'crim/fl/pinellas/dwlsr/horrox.html')
            elif judge == 'levine':
                return render(request, 'crim/fl/pinellas/dwlsr/levine.html')
            elif judge == 'mckyton':
                return render(request, 'crim/fl/pinellas/dwlsr/mckyton.html')
            elif judge == 'overton':
                return render(request, 'crim/fl/pinellas/dwlsr/overton.html')
            elif judge == 'pierce':
                return render(request, 'crim/fl/pinellas/dwlsr/pierce.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/pinellas/dwlsr/dwlsr.html')

    else:
        pinell_judge = PinellasJudges()

    return render(request, 'crim/fl/pinellas/dwlsr.html', {'pinell_judge': pinell_judge})

def dwlsr(request):
    return render(request, 'crim/fl/pinellas/dwlsr/dwlsr.html')

def bedinghaus(request):
    return render(request, 'crim/fl/pinellas/dwlsr/bedinghaus.html')

def carballo(request):
    return render(request, 'crim/fl/pinellas/dwlsr/carballo.html')

def dittmer(request):
    return render(request, 'crim/fl/pinellas/dwlsr/dittmer.html')

def horrox(request):
    return render(request, 'crim/fl/pinellas/dwlsr/horrox.html')

def levine(request):
    return render(request, 'crim/fl/pinellas/dwlsr/levine.html')

def mckyton(request):
    return render(request, 'crim/fl/pinellas/dwlsr/mckyton.html')

def overton(request):
    return render(request, 'crim/fl/pinellas/dwlsr/overton.html')

def pierce(request):
    return render(request, 'crim/fl/pinellas/dwlsr/pierce.html')
