
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *
from crim.models import search_all

def hillsborough_petit_theft_specific(request):
    party_name = ClientIdentification(request)
    print("Hillsborough Page")

    if request.method == 'POST':
        print("Hello")
        party_name = ClientIdentification(request.POST)

        if party_name.is_valid():

            first = party_name.cleaned_data['first']
            last = party_name.cleaned_data['last']
            county = "hill"
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

            if 'Farr' in str(judge):

                return render(request,
                                'crim/fl/hills/petit-theft/farr-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                'date': date,
                                'case_number': case_number,
                                })
            elif 'Conrad' in str(judge):
                return render(request, 'crim/fl/hills/petit-theft/conrad-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'Jeske' in str(judge):
                return render(request, 'crim/fl/hills/petit-theft/jeske-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif  'Lefler' in str(judge):
                return render(request, 'crim/fl/hills/petit-theft/lefler-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'McNeil' in str(judge):
                return render(request, 'crim/fl/hills/petit-theft/mcneil-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'Myers' in str(judge):
                return render(request, 'crim/fl/hills/petit-theft/myers-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            elif 'Taylor' in str(judge):
                return render(request, 'crim/fl/hills/petit-theft/taylor-petit-theft-specific.html',
                                {
                                'first': first,
                                'last': last,
                                })
            else:
                return render(request, 'crim/fl/hills/petit-theft/petit-theft.html',
                                {
                                'first': first,
                                'last': last,
                                })

    else:

        party_name = ClientIdentification()

    return render(request, 'crim/fl/hills/hillsborough-petit-theft-case-search.html',
                            {
                            'party_name': party_name,
                            })

def petit_theft(request):
    client_identification = ClientIdentification(request)
    if request.method == 'POST':
        client_identification = ClientIdentification(request.POST)
    else:
        client_identification = ClientIdentification()
    return render(request, 'crim/fl/hills/petit-theft/petit-theft.html', {'client_identification': client_identification})


def farr_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/farr-petit-theft-specific.html')

def conrad_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/conrad-petit-theft-specific.html')

def lefler_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/lefler-petit-theft-specific.html')

def jeske_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/jeske-petit-theft-specific.html')

def mcneil_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/mcneil-petit-theft-specific.html')

def myers_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/myers-petit-theft-specific.html')

def taylor_specific(request):
    return render(request, 'crim/fl/hills/petit-theft/taylor-petit-theft-specific.html')
