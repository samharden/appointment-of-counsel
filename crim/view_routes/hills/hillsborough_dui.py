
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *
from crim.models import search_all

def hillsborough_dui(request):
    party_name = ClientIdentification(request)

    print("Hillsborough Page")

    if request.method == 'POST':
        print("Hello")
        party_name = ClientIdentification(request.POST)

        if party_name.is_valid():

            notsure = party_name.cleaned_data['notsure']
            print(notsure)
            if str(notsure) == 'True':
                return render(request, 'crim/fl/hills/dui/dui.html')

            elif str(notsure) == 'False':
                first = party_name.cleaned_data['first']
                last = party_name.cleaned_data['last']
                county = "hill"
                print(first, last)
                #search_all(first, last, county)
                (judge, case_number, date, appearance_type) = search_all(first, last, county)
                judge = str(judge)
                # if ''
                print("Views says the judge is", judge)
                print("Views says the date is", date)
                print("Views says appearance type is", appearance_type)
                if 'Farr' in str(judge):

                    return render(request,
                                    'crim/fl/hills/dui/farrdui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                elif 'Greco' in str(judge):
                    return render(request, 'crim/fl/hills/dui/grecodui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                elif 'Jeske' in str(judge):
                    return render(request, 'crim/fl/hills/dui/jeskedui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                elif  'Lefler' in str(judge):
                    return render(request, 'crim/fl/hills/dui/leflerdui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                elif 'McNeil' in str(judge):
                    return render(request, 'crim/fl/hills/dui/mcneildui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                elif 'Myers' in str(judge):
                    return render(request, 'crim/fl/hills/dui/myersdui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                elif 'Taylor' in str(judge):
                    return render(request, 'crim/fl/hills/dui/taylordui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })
                else:
                    return render(request, 'crim/fl/hills/dui/dui.html',
                                    {
                                    'first': first,
                                    'last': last,
                                    })

    else:

        party_name = ClientIdentification()

    return render(request, 'crim/fl/hills/hillsborough-dui.html',
                            {'party_name': party_name})

def dui(request):
    client_identification = ClientIdentification(request)
    if request.method == 'POST':
        client_identification = ClientIdentification(request.POST)
    else:
        client_identification = ClientIdentification()
    return render(request, 'crim/fl/hills/dui/dui.html', {'client_identification': client_identification})

def farr(request):
    return render(request, 'crim/fl/hills/dui/farrdui.html')

def greco(request):
    return render(request, 'crim/fl/hills/dui/grecodui.html')

def lefler(request):
    return render(request, 'crim/fl/hills/dui/leflerdui.html')

def jeske(request):
    return render(request, 'crim/fl/hills/dui/jeskedui.html')

def mcneil(request):
    return render(request, 'crim/fl/hills/dui/mcneildui.html')

def myers(request):
    return render(request, 'crim/fl/hills/dui/myersdui.html')

def taylor(request):
    return render(request, 'crim/fl/hills/dui/taylordui.html')
