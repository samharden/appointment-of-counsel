from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from fl_discrim_helper.forms import *
from fl_discrim_helper.view_routes import (
                                    choose_complaint_type,
                                    pub_acc_complaint,
                                    )


def choose_complaint_type(request):
    complaint_type_form = DiscrimCaseTypeForm(request)

    if request.method == 'POST':

        complaint_type_form = DiscrimCaseTypeForm(request.POST)

        if complaint_type_form.is_valid():

            #complaint_type = complaint_type_form.cleaned_data['case_type']
            complaint_type = request.POST.get('case_type')
            request.session['complaint_type'] = complaint_type


            if complaint_type == 'employment':
                return HttpResponse(complaint_type)
            elif complaint_type == 'pubacc':

                print(complaint_type)
                # return render(request, 'fl-discrim-helper/pub-acc-complaint.html', complaint_type)
                return HttpResponseRedirect('pub-acc-complaint.html', complaint_type)
                #return render(request, 'fl-discrim-helper/pub-acc-complaint.html', complaint_type)
            elif complaint_type == 'housing':
                return HttpResponse('housing')

    else:
        complaint_type_form = DiscrimCaseTypeForm()

    return render(request, 'fl-discrim-helper/choose-complaint-type.html', {'complaint_type_form': complaint_type_form})
