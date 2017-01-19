from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from fl_discrim_helper.form_folder.pub_acc_complaint_form import *
#from fl_discrim_helper.forms import *
from fl_discrim_helper.view_routes import (
                                    choose_complaint_type,

                                    )



def pub_acc_complaint(request):
    print("Help")
    complaint_type = request.session['complaint_type']
    print(complaint_type)

    cx_pub_acc_form = CxPubAccForm(request)
    op_pub_acc_form = OpPubAccForm(request)
    disorg_pub_acc_form = DisOrgPubAccForm(request)
    reporg_pub_acc_form = RepOrgPubAccForm(request)
    disreason_pub_acc_form = DisReasonPubAccForm(request)

    if request.method == 'POST':

        cx_pub_acc_form = CxPubAccForm(request.POST)
        op_pub_acc_form = OpPubAccForm(request.POST)
        disorg_pub_acc_form = DisOrgPubAccForm(request.POST)
        reporg_pub_acc_form = RepOrgPubAccForm(request.POST)
        disreason_pub_acc_form = DisReasonPubAccForm(request)

        if cx_pub_acc_form.is_valid():
            print("Valid")
            cx_state = request.POST.get('cx_state')
            print(cx_state)
            request.session['cx_state'] = cx_state

            cx_first_name = request.POST.get('cx_first_name')
            print(cx_first_name)
            request.session['cx_first_name'] = cx_first_name



    else:
        cx_pub_acc_form = CxPubAccForm()
        op_pub_acc_form = OpPubAccForm()
        disorg_pub_acc_form = DisOrgPubAccForm()
        reporg_pub_acc_form = RepOrgPubAccForm()
        disreason_pub_acc_form = DisReasonPubAccForm()


    return render(request,
                    'fl-discrim-helper/pub-acc-complaint.html',
                    {'cx_pub_acc_form': cx_pub_acc_form,
                    'op_pub_acc_form': op_pub_acc_form,
                    'disorg_pub_acc_form': disorg_pub_acc_form,
                    'reporg_pub_acc_form': reporg_pub_acc_form,
                    'disreason_pub_acc_form': disreason_pub_acc_form,
                    }
                    )



#
