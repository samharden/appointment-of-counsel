
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from small_claims.form_folder.small_claim_auto import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def sc_complaint_auto(request):

    header_info = HeaderInfo(request)
    location_info = LocationInfo(request)
    amount_info = AmountInfo(request)
    description_info = DescriptionInfo(request)


    if request.method == 'POST':

        header_info = HeaderInfo(request.POST)
        location_info = LocationInfo(request.POST)
        amount_info = AmountInfo(request.POST)
        description_info = DescriptionInfo(request.POST)


        circuit = ''
        if header_info.is_valid():
            print("Valid")

            county = request.POST.get('county')
            if county == 'HILLSBOROUGH':
                circuit = 'THIRTEENTH'
            elif county == 'PINELLAS':
                circuit = 'SIXTH'
            elif county == 'PASCO':
                circuit = 'SIXTH'
            else:
                circuit = '__________'
            respondent = request.POST.get('respondent')
            petitioner = request.POST.get('petitioner')


            petitioner_address = request.POST.get('petitioner_address')
            petitioner_city = request.POST.get('petitioner_city')
            petitioner_state = request.POST.get('petitioner_state')
            petitioner_zip = request.POST.get('petitioner_zip')
            petitioner_phone = request.POST.get('petitioner_phone')
            respondent_address = request.POST.get('respondent_address')
            respondent_city = request.POST.get('respondent_city')
            respondent_state = request.POST.get('respondent_state')
            respondent_zip = request.POST.get('respondent_zip')
            amount_info = request.POST.get('amount')
            date_of_accident = request.POST.get('date_of_accident')
            city_of_accident = request.POST.get('city_of_accident')
            physical_injuries = request.POST.get('physical_injuries')

            if physical_injuries == 'Yes':
                injury_desc = " and Plaintiff has suffered physical injuries."
            elif physical_injuries == 'No':
                injury_desc = "."

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s-vs-%s\
                                                complaint.pdf"' % (petitioner, respondent)

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

            styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
            respondent_text = '<font size=12> <style="right"> <b>Case No: _______________ </b><br></br> \
                    <b>Division: _____________</b>\
                    </style></font>'

            Complaint.append(Paragraph(respondent_text, styles["Right"]))
            Complaint.append(Spacer(1, 0))

            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            respondent_text = '<font size=12> <style="justify"> <b> %s, <br></br> Plaintiff,<br></br>\
                    %s <br></br>\
                    %s, %s &nbsp %s \
                    </b></style></font>' % (petitioner, petitioner_address, petitioner_city, petitioner_state, petitioner_zip)

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            vs = '<font size=14> <style="left"> <b>vs. \
                    </b></style></font>'

            Complaint.append(Paragraph(vs, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            respondent_text = '<font size=12> <style="justify"> <b> %s, <br></br> Defendant,<br></br>\
                    %s <br></br>\
                    %s, %s &nbsp %s \
                    </b></style></font>' % (respondent, respondent_address, respondent_city, respondent_state, respondent_zip)

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            title = '<font size=14> <style="center"> <b>STATEMENT OF CLAIM FOR AUTOMOBILE NEGLIGENCE\
                    </b></style></font>'

            Complaint.append(Paragraph(title, styles["Center"]))
            Complaint.append(Spacer(1, 12))


            intro_text = '<font size=12> <style="justify"> <b> &nbsp &nbsp &nbsp Plaintiff %s \
                    sues Defendant, %s, and alleges:\
                    </b></style></font>' % (petitioner, respondent)

            Complaint.append(Paragraph(intro_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            one_text = '<font size=12> <style="justify"> <b> 1. &nbsp &nbsp This \
                    is an action for damages which does not exceed $5,000.00.\
                    </b></style></font>'

            Complaint.append(Paragraph(one_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            two_text = "<font size=12> <style='justify'> <b> 2. &nbsp On or about \
                    %s in the vicinity of %s, on a public highway in %s County, Florida, \
                    Plaintiff's motor vehicle, being operated and owned by %s \
                    collided with Defendant's motor vehicle, being operated and \
                    owned by %s.\
                    </b></style></font>" % (date_of_accident, city_of_accident, county, petitioner, respondent)

            Complaint.append(Paragraph(two_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            three_text = "<font size=12> <style='justify'> <b> 3. &nbsp The collision\
                    was caused by Defendant's negligent and careless operation of their\
                    vehicle, whereby Plaintiff's vehicle was damaged and depreciated in\
                    value%s\
                    </b></style></font>" % injury_desc

            Complaint.append(Paragraph(three_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))




            wherefore_text = '<font size=12> <style="justify"> <b> WHEREFORE \
                    Plaintiff demands judgement in the amount of $%s, plus all \
                    costs of this action.\
                    </b></style></font>' % amount_info

            Complaint.append(Paragraph(wherefore_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            swear_text = '<font size=12> <style="justify"> <b> %s being first \
                    duly sworn on oath, says the foregoing is a just and true \
                    statement of the amount owing by defendant to plaintiff, \
                    exclusive of all set-offs and just grounds of defense.\
                    </b></style></font>' % petitioner

            Complaint.append(Paragraph(swear_text, styles["Justify"]))
            Complaint.append(Spacer(1, 36))


            respondent_text = '<font size=12> <style="right"> <b>_____________________</b><br></br> \
                    %s &nbsp &nbsp &nbsp &nbsp </style></font>' % petitioner

            Complaint.append(Paragraph(respondent_text, styles["Right"]))
            Complaint.append(Spacer(1, 0))

            Complaint.append(PageBreak())

            respondent_text = '<font size=12> <style="left"> <b>STATE OF FLORIDA</b><br></br> \
                    <b>COUNTY OF %s</b><br></br> \
                    </style></font>' % county.upper()

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            respondent_text = '<font size=12> <style="left"> <b>The foregoing instrument was  \
                    sworn to or affirmed and signed before me this ____ day of ______________, 20__, \
                    by %s who is personally known to me or has produced _____________________ identification\
                    and who <br></br> [ ] did <br></br> [ ] did not <br></br> take an oath.\
                    </b></style></font>' % petitioner

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))
            Complaint.append(Spacer(1, 28))

            respondent_text = '<font size=12> <style="left"> <b>_____________________  \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp _______________________<br></br>  \
                    &nbsp As Deputy Clerk \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    Notary Public\
                    </b></style></font>'

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))
            Complaint.append(Spacer(1, 14))

            respondent_text = '<font size=12> <style="left"> <b>_____________________  \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp _______________________<br></br>  \
                    &nbsp Printed Name \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp \
                    &nbsp &nbsp &nbsp Printed Name\
                    </b></style></font>'

            Complaint.append(Paragraph(respondent_text, styles["Justify"]))
            Complaint.append(Spacer(1, 14))



            doc.build(Complaint)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    else:
        header_info = HeaderInfo()
        location_info = LocationInfo()
        amount_info = AmountInfo()
        description_info = DescriptionInfo()

    return render(request,'fl-small-claims/small-claim-auto.html',
                    {'header_info': header_info,
                    'location_info': location_info,
                    'amount_info': amount_info,
                    'description_info': description_info,


                    })
