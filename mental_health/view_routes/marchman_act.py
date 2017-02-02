
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from mental_health.form_folder.marchman_act_forms import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def marchman_act(request):

    header_info = HeaderInfo(request)
    location_info = LocationInfo(request)
    relationship_info = RelationshipInfo(request)
    good_terms_info = GoodTermsInfo(request)
    previous_allegations_info = PreviousAllegationsInfo(request)

    if request.method == 'POST':

        header_info = HeaderInfo(request.POST)
        location_info = LocationInfo(request.POST)
        relationship_info = RelationshipInfo(request.POST)
        good_terms_info = GoodTermsInfo(request.POST)
        previous_allegations_info = PreviousAllegationsInfo(request.POST)
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
            respondent_age = request.POST.get('respondent_age')
            respondent_age_choose = request.POST.get('respondent_age_choose')

            petitioner_address = request.POST.get('petitioner_address')
            petitioner_city = request.POST.get('petitioner_city')
            petitioner_state = request.POST.get('petitioner_state')
            petitioner_zip = request.POST.get('petitioner_zip')
            petitioner_phone = request.POST.get('petitioner_phone')
            respondent_address = request.POST.get('respondent_address')
            respondent_city = request.POST.get('respondent_city')
            respondent_state = request.POST.get('respondent_state')
            respondent_zip = request.POST.get('respondent_zip')

            respondent_address_alt = request.POST.get('respondent_address_alt')
            respondent_city_alt = request.POST.get('respondent_city_alt')
            respondent_state_alt = request.POST.get('respondent_state_alt')
            respondent_zip_alt = request.POST.get('respondent_zip_alt')

            relationship = request.POST.get('relationship')

            good_terms = request.POST.get('good_terms')
            good_terms_describe = request.POST.get('good_terms_describe')

            previous_allegation_p = request.POST.get('previous_allegation_p')
            previous_allegation_p_describe = request.POST.get('previous_allegation_p_describe')

            previous_allegation_r = request.POST.get('previous_allegation_r')
            previous_allegation_r_describe = request.POST.get('previous_allegation_r_describe')

            previous_crim = request.POST.get('previous_crim')
            previous_court_case = request.POST.get('previous_court_case')
            previous_court_case_describe = request.POST.get('previous_court_case_describe')

            how_long_known = request.POST.get('how_long_known')
            length_of_substance = request.POST.get('length_of_substance')
            length_of_substance_time = request.POST.get('length_of_substance_time')

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s-marchman-\
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


            intro_text = '<font size=12> <style="justify"> <b>I, %s \
                    being duly sworn, am filing this sworn statement requesting \
                    a court order for the involuntary assessment of %s\
                    </b></style></font>' % (petitioner, respondent)

            Complaint.append(Paragraph(intro_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            age_text = '<font size=12> <style="justify"> <b>Is\
                    the Person 18 years of age or over? %s. Their age: %s\
                    </b></style></font>' % (respondent_age_choose, respondent_age)

            Complaint.append(Paragraph(age_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            text = '<font size=12> <style="justify"> <b>The petition and affidavit \
            will be included in the Person’s clinical record and may be viewed by \
            the Person. I understand that by filling out this form, the Person may \
            be taken by law enforcement to a hospital or licensed substance abuse \
            facility for assessment and stabilization.<br></br> <br></br>\
            I SWEAR that the answers to the following questions are given honestly, \
            in good faith, and to the best of my knowledge.\
                    </b></style></font>'

            Complaint.append(Paragraph(text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            address_text = '<font size=12> <style="justify"> <b>1. a. Petitioner \
                    lives at the following address: <br></br><br></br></b> \
                    &nbsp &nbsp &nbsp &nbsp %s, %s, %s, %s <br></br><br></br>\
                    &nbsp &nbsp &nbsp &nbsp Phone: %s \
                    </style></font>' % (petitioner_address,
                                        petitioner_city,
                                        petitioner_state,
                                        petitioner_zip,
                                        petitioner_phone,
                                        )

            Complaint.append(Paragraph(address_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            doc.build(Complaint)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    else:
        header_info = HeaderInfo()
        location_info = LocationInfo()
        relationship_info = RelationshipInfo(request.POST)
        good_terms_info = GoodTermsInfo(request.POST)
        previous_allegations_info = PreviousAllegationsInfo(request.POST)

    return render(request,'fl-mental-health/marchman-act.html',
                    {'header_info': header_info,
                    'location_info': location_info,
                    'relationship_info': relationship_info,
                    'good_terms_info': good_terms_info,
                    'previous_allegations_info': previous_allegations_info,
                    })
