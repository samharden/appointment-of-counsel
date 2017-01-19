
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def hillsborough_dwlsr(request):
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
                return render(request, 'crim/fl/hills/dwlsr/farr.html')
            elif judge == 'greco':
                return render(request, 'crim/fl/hills/dwlsr/greco.html')
            elif judge == 'jeske':
                return render(request, 'crim/fl/hills/dwlsr/jeske.html')
            elif judge == 'lefler':
                return render(request, 'crim/fl/hills/dwlsr/lefler.html')
            elif judge == 'mcneil':
                return render(request, 'crim/fl/hills/dwlsr/mcneil.html')
            elif judge == 'myers':
                return render(request, 'crim/fl/hills/dwlsr/myers.html')
            elif judge == 'taylor':
                return render(request, 'crim/fl/hills/dwlsr/taylor.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/hills/dwlsr/dwlsr.html')

    else:
        hillsb_judge = HillsboroughJudges()

    return render(request, 'crim/fl/hills/hillsborough-dwlsr.html', {'hillsb_judge': hillsb_judge})

def dwlsr(request):
    return render(request, 'crim/fl/hills/dwlsr/dwlsr.html')

def farr(request):
    return render(request, 'crim/fl/hills/dwlsr/farr.html')

def greco(request):
    return render(request, 'crim/fl/hills/dwlsr/greco.html')

def lefler(request):
    return render(request, 'crim/fl/hills/dwlsr/lefler.html')

def jeske(request):
    return render(request, 'crim/fl/hills/dwlsr/jeske.html')

def mcneil(request):
    return render(request, 'crim/fl/hills/dwlsr/mcneil.html')

def myers(request):
    return render(request, 'crim/fl/hills/dwlsr/myers.html')

def taylor(request):
    return render(request, 'crim/fl/hills/dwlsr/taylor.html')
