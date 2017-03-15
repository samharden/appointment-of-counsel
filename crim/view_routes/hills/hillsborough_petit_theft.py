
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def hillsborough_petit_theft(request):
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
                return render(request, 'crim/fl/hills/petit-theft/farr.html')
            elif judge == 'conrad':
                return render(request, 'crim/fl/hills/petit-theft/conrad.html')
            elif judge == 'jeske':
                return render(request, 'crim/fl/hills/petit-theft/jeske.html')
            elif judge == 'lefler':
                return render(request, 'crim/fl/hills/petit-theft/lefler.html')
            elif judge == 'mcneil':
                return render(request, 'crim/fl/hills/petit-theft/mcneil.html')
            elif judge == 'myers':
                return render(request, 'crim/fl/hills/petit-theft/myers.html')
            elif judge == 'taylor':
                return render(request, 'crim/fl/hills/petit-theft/taylor.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/hills/petit-theft/petittheft.html')

    else:
        hillsb_judge = HillsboroughJudges()

    return render(request, 'crim/fl/hills/hillsborough-petit-theft.html', {'hillsb_judge': hillsb_judge})

def petit_theft(request):
    return render(request, 'crim/fl/hills/petit-theft/petittheft.html')

def farr(request):
    return render(request, 'crim/fl/hills/petit-theft/farr.html')

def conrad(request):
    return render(request, 'crim/fl/hills/petit-theft/conrad.html')

def lefler(request):
    return render(request, 'crim/fl/hills/petit-theft/lefler.html')

def jeske(request):
    return render(request, 'crim/fl/hills/petit-theft/jeske.html')

def mcneil(request):
    return render(request, 'crim/fl/hills/petit-theft/mcneil.html')

def myers(request):
    return render(request, 'crim/fl/hills/petit-theft/myers.html')

def taylor(request):
    return render(request, 'crim/fl/hills/petit-theft/taylor.html')
