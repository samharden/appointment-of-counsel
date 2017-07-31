
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from appointment.form_folder.appointment_form import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import date

def form_fill(request):

    form_info = FormInfo(request)


    if request.method == 'POST':

        form_info = FormInfo(request.POST)


        circuit = ''
        if form_info.is_valid():
            print("Valid")

            county = request.POST.get('county')
            defendant_name = request.POST.get('defendant_name')
            case_no = request.POST.get('case_no')
            charges = request.POST.get('charges')
            courthouse_name = request.POST.get('courthouse_name')
            judge = request.POST.get('judge')
            today_date = str(date.today())
            day = today_date[8:10]
            month = today_date[5:7]
            year = today_date[:4]
            today_date = month+'/'+day+'/'+year
            hearing_date = request.POST.get('hearing_date')




            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s-appointment\
                                                -form.pdf"' % defendant_name

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer,
                                    pagesize=letter,
                                    rightMargin=72,leftMargin=72,
                                    topMargin=72,bottomMargin=50)
            Appointment=[]

            styles=getSampleStyleSheet()

            ### HEADER TEXT ###

            styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
            header_text = '<font size=14> <style="center"> <b>IN THE CIRCUIT COURT \
                    OF %s COUNTY, WEST VIRGINIA <br></br> \
                    </b></style></font>' % county

            Appointment.append(Paragraph(header_text, styles["Center"]))
            Appointment.append(Spacer(1, 12))

            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            plaintiff_text = '<font size=12> <style="justify"> <b> STATE of WEST VIRGINIA</b></style></font><br></br>'

            Appointment.append(Paragraph(plaintiff_text, styles["Justify"]))
            Appointment.append(Spacer(1, 12))

            styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
            respondent_text = '<font size=12> <style="right"> <b>Case No: %s </b><br></br> \
                    </style></font>' % case_no

            Appointment.append(Paragraph(respondent_text, styles["Right"]))
            Appointment.append(Spacer(1, 0))

            vs = '<font size=14> <style="left"> <b>vs. \
                    </b></style></font>'

            Appointment.append(Paragraph(vs, styles["Justify"]))
            Appointment.append(Spacer(1, 12))


            defendant_text = '<font size=12> <style="justify"> <b> %s, <br></br> Defendant,<br></br>\
                    </b></style></font>' % defendant_name
            Appointment.append(Paragraph(defendant_text, styles["Justify"]))
            Appointment.append(Spacer(1, 12))


            title = '<font size=14> <style="center"> <b>APPOINTMENT ORDER \
                    </b></style></font>'

            Appointment.append(Paragraph(title, styles["Center"]))
            Appointment.append(Spacer(1, 12))


            intro_text = '<font size=12> <style="justify"> <b> &nbsp &nbsp &nbsp On this date %s \
                    it is made known to the Court that the Defendant, %s, \
                    was charged with the crime of %s, in case number %s.\
                    </b></style></font>' % (today_date, defendant_name, charges, case_no)

            Appointment.append(Paragraph(intro_text, styles["Justify"]))
            Appointment.append(Spacer(1, 12))

            one_text = '<font size=12> <style="justify"> <b> It is further made \
                    known to the Court that %s is a pauper, a financial affidavit\
                     having been filed herein, and desires to have counsel appointed \
                     to represent him/her in this matter.\
                    </b></style></font>' % defendant_name

            Appointment.append(Paragraph(one_text, styles["Justify"]))
            Appointment.append(Spacer(1, 12))

            two_text = '<font size=12> <style="justify"> <b> Therefore it is ORDERED \
                    that the Lawyer JAMES TIU, ID NUMBER 234-02-9904 is hereby \
                    appointed to represent %s as counsel, the date of the first \
                    hearing, if known, is %s in the Circuit Court of %s County.\
                    </b></style></font>' % (defendant_name, hearing_date, county)

            Appointment.append(Paragraph(two_text, styles["Justify"]))
            Appointment.append(Spacer(1, 12))


            respondent_text = '<font size=12> <style="right"> So Entered on this Date %s\
                    <br></br><br></br><br></br>\
                    <b>_____________________</b><br></br> \
                    Circuit Judge %s &nbsp &nbsp &nbsp &nbsp </style></font>' % (today_date, judge)

            Appointment.append(Paragraph(respondent_text, styles["Right"]))
            Appointment.append(Spacer(1, 0))


            doc.build(Appointment)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    else:
        form_info = FormInfo()


    return render(request,'appointment/form.html',
                    {'form_info': form_info,

                    })
