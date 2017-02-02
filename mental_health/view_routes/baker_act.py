
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from mental_health.form_folder.baker_act_forms import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def baker_act(request):

    header_info = HeaderInfo(request)
    location_info = LocationInfo(request)

    if request.method == 'POST':

        header_info = HeaderInfo(request.POST)
        location_info = LocationInfo(request.POST)
        circuit = ''
        if header_info.is_valid():
            print("Valid")

            county = request.POST.get('county')
            if county == 'HILLSBOROUGH':
                circuit = 'THIRTEENTH'
            elif county == 'PINELLAS':
                circuit = 'SIXTH'
            else:
                circuit = '__________'
            respondent = request.POST.get('respondent')
            petitioner = request.POST.get('petitioner')

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s-baker-\
                                                act-petition.pdf"' % respondent
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer,
                                    pagesize=letter,
                                    rightMargin=72,leftMargin=72,
                                    topMargin=72,bottomMargin=50)
            Complaint=[]

            styles=getSampleStyleSheet()

            ### HEADER TEXT ###

            styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
            header_text = '<font size=14> <style="center"> <b>IN THE CIRCUIT COURT \
                    OF THE %s JUDICIAL CIRCUIT <br></br> \
                    IN AND FOR %s COUNTY, FLORIDA <br></br> \
                    </b></style></font>' % (circuit, county)

            Complaint.append(Paragraph(header_text, styles["Center"]))
            Complaint.append(Spacer(1, 12))

            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            respondent_text = '<font size=14> <style="justify"> <b>IN RE: %s \
                    </b></style></font>' % respondent

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))

            styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
            respondent_text = '<font size=14> <style="right"> <b>Case No: _______________ \
                    </b></style></font>'

            Complaint.append(Paragraph(respondent_text, styles["Right"]))
            Complaint.append(Spacer(1, 24))

            title = '<font size=14> <style="center"> <b>PETITION AND AFFIDAVIT \
                    FOR INVOLUNTARY ASSESSMENT AND STABILIZATION \
                    </b></style></font>'

            Complaint.append(Paragraph(title, styles["Center"]))
            Complaint.append(Spacer(1, 12))


            intro_text = '<font size=14> <style="justify"> <b>I, %s \
                    being duly sworn, am filing this sworn statement requesting \
                    a court order for the involuntary assessment of %s\
                    </b></style></font>' % (petitioner, respondent)

            Complaint.append(Paragraph(intro_text, styles["Justify"]))





            doc.build(Complaint)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    else:
        header_info = HeaderInfo()
        location_info = LocationInfo()

    return render(request,'fl-mental-health/baker-act.html',
                    {'header_info': header_info,
                    'location_info': location_info,
                    })
