
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *
from crim.models import search_all

def pinellas_dwlsr_specific(request):
    party_name = ClientIdentification(request)
    print("Pinellas DWLSR Case Search Page")

    if request.method == 'POST':
        print("Hello")
        party_name = ClientIdentification(request.POST)

        if party_name.is_valid():

            first = party_name.cleaned_data['first']
            last = party_name.cleaned_data['last']
            county = "pine"
            print(first, last)
            #search_all(first, last, county)
            (judge, case_number, date, appearance_type) = search_all(first, last, county)
            judge = str(judge)
            # if ''
            date = str(date)
            case_number = str(case_number)
            case_number = case_number.split('\n')[0]
            case_number = case_number.split(' ')[4]
            print("Views says the judge is", judge)
            print("Views says the date is", date)

            if 'HORROX' in str(judge):

                return render(request,
                                'crim/fl/pinellas/dwlsr/horrox-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'BEDINGHAUS' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/bedinghaus-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'CARBALLO' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/carballo-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif  'DITTMER' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/dittmer-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'LEVINE' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/levine-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'MCKYTON' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/mckyton-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'OVERTON' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/overton-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'PIERCE' in str(judge):
                return render(request, 'crim/fl/pinellas/dwlsr/pierce-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            else:
                return render(request, 'crim/fl/pinellas/dwlsr/dwlsr.html',
                                {
                                'first': first,
                                'last': last,
                                })

    else:

        party_name = ClientIdentification()

    return render(request, 'crim/fl/pinellas/dwlsr-case-search.html',
                            {
                            'party_name': party_name,
                            })
