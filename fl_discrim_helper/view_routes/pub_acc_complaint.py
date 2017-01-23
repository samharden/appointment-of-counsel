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
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


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
        disreason_pub_acc_form = DisReasonPubAccForm(request.POST)

        if cx_pub_acc_form.is_valid():
            print("Valid")
            cx_state = request.POST.get('cx_state')
            print(cx_state)
            request.session['cx_state'] = cx_state

            cx_last_name = request.POST.get('cx_last_name')
            print(cx_last_name)
            request.session['cx_last_name'] = cx_last_name

            from fl_discrim_helper.view_routes.pub_acc_cx_pdf import pub_acc_cx_pdf

            

            p = pub_acc_cx_pdf(request, cx_last_name)

            # response = pub_acc_cx_pdf(cx_last_name)

            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="filename.pdf"'

            # p = canvas.Canvas(response)
            # p.drawString(100, 800, cx_first_name)
            # #
            # p.showPage()
            # p.save()




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
