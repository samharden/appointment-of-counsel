
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

# from crim.templates.crim.fl.hills.battery import hillsborough_battery

# Create your views here.


def index(request):
    crimform = CrimCaseTypeForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        crimform = CrimCaseTypeForm(request.POST)

        if crimform.is_valid():
            print("Valid index")
            case_type = crimform.cleaned_data['case_type']
            print(case_type)
            scs = crimform.cleaned_data['sepcific_case_search']
            county = crimform.cleaned_data['county']
            print(county)

            if case_type == 'dui' and county == 'hillsb' and scs == 'yes':
                hillsb_judge = HillsboroughJudges()

                return HttpResponseRedirect('fl/hills/hillsborough-dui-case-search.html')

            elif case_type == 'dui' and county == 'hillsb' and scs == 'no':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-dui.html')

            elif case_type == 'battery' and county == 'hillsb' and scs == 'yes':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-battery-case-search.html')

            elif case_type == 'battery' and county == 'hillsb' and scs == 'no':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-battery.html')

            elif case_type == 'marijuanaposs' and county == 'hillsb' and scs == 'no':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-marijuanaposs.html')

            elif case_type == 'marijuanaposs' and county == 'hillsb' and scs == 'yes':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-marijuana-possession-case-search.html')

            elif case_type == 'petit-theft' and county == 'hillsb' and scs == 'no':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-petit-theft.html')

            elif case_type == 'petit-theft' and county == 'hillsb' and scs == 'yes':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-petit-theft-case-search.html')

            elif case_type == 'dwlsr' and county == 'hillsb' and scs == 'yes':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-dwlsr-case-search.html')

            elif case_type == 'dwlsr' and county == 'hillsb' and scs == 'no':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-dwlsr.html')

            #####################################################################

            elif case_type == 'dui' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/pinellas-dui.html')

            elif case_type == 'marijuanaposs' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/marijuana-possession.html')

            elif case_type == 'battery' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/battery.html')

            elif case_type == 'dwlsr' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/dwlsr.html')

            elif case_type == 'petit-theft' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/petit-theft.html')


        else:
            crimform = CrimCaseTypeForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        crimform = CrimCaseTypeForm()


    print("Top of index")


    return render(request, 'crim/index.html', {'crimform': crimform})
