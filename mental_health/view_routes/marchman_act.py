
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
from mental_health.models import *

def marchman_act(request):

    header_info = HeaderInfo(request)
    location_info = LocationInfo(request)
    relationship_info = RelationshipInfo(request)
    good_terms_info = GoodTermsInfo(request)
    previous_allegations_info = PreviousAllegationsInfo(request)
    knowledge_sub_abuse_info = KnowledgeAboutPersonInfo(request)
    identifying_info = IdentifyingInfo(request)
    picture_form = PictureID(request)
    violence_info = ViolenceInfo(request)
    atty_guardian_info = AttyGuardianInfo(request)

    if request.method == 'POST':

        header_info = HeaderInfo(request.POST)
        location_info = LocationInfo(request.POST)
        relationship_info = RelationshipInfo(request.POST)
        good_terms_info = GoodTermsInfo(request.POST)
        previous_allegations_info = PreviousAllegationsInfo(request.POST)
        knowledge_sub_abuse_info = KnowledgeAboutPersonInfo(request.POST)
        identifying_info = IdentifyingInfo(request.POST)
        picture_form = PictureID(request.POST, request.FILES)
        violence_info = ViolenceInfo(request.POST)
        atty_guardian_info = AttyGuardianInfo(request.POST)

        circuit = ''

        description_placeholder = ''
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
            if good_terms == "Yes":
                good_terms_choice = ""
            elif good_terms == "No":
                good_terms_choice = "NOT"

            good_terms_describe = request.POST.get('good_terms_describe')

            previous_allegation_p = request.POST.get('previous_allegation_p')
            if previous_allegation_p == "Yes":
                previous_allegation_p_choice = "have"
            elif previous_allegation_p == "No":
                previous_allegation_p_choice = "have not"

            previous_allegation_p_describe = request.POST.get('previous_allegation_p_describe')

            previous_allegation_r = request.POST.get('previous_allegation_r')
            if previous_allegation_r == "Yes":
                previous_allegation_r_choice = "have"
            elif previous_allegation_r == "No":
                previous_allegation_r_choice = "have not"
            previous_allegation_r_describe = request.POST.get('previous_allegation_r_describe')

            previous_crim = request.POST.get('previous_crim')
            if previous_crim == "Yes":
                previous_crim_choice = "has"
            elif previous_crim == "No":
                previous_crim_choice = "has not"

            previous_court_case = request.POST.get('previous_court_case')
            if previous_court_case == "Yes":
                previous_court_case = "I or a family member am not now, and have not in the past, been involved in a court case with the Person."
            elif previous_court_case == "No":
                previous_court_case = " I or a family member am now, or was, involved in a court case with the Person.  This case is/was a:"


            previous_court_case_describe = request.POST.get('previous_court_case_describe')

            how_long_known = request.POST.get('how_long_known')
            length_of_substance = request.POST.get('length_of_substance')
            length_of_substance_time = request.POST.get('length_of_substance_time')

            question_9 = request.POST.get('question_9')
            question_9_desc = request.POST.get('question_9_desc')
            question_10 = request.POST.get('question_10')
            question_10_desc = request.POST.get('question_10_desc')
            question_11 = request.POST.get('question_11')
            question_11_desc = request.POST.get('question_11_desc')
            question_12 = request.POST.get('question_12')
            question_12_desc = request.POST.get('question_12_desc')
            question_13 = request.POST.get('question_13')
            question_13_desc = request.POST.get('question_13_desc')
            question_14 = request.POST.get('question_14')
            question_14_desc = request.POST.get('question_14_desc')
            question_15a = request.POST.get('question_15a')
            question_15a_desc = request.POST.get('question_15a_desc')
            question_15b = request.POST.get('question_15b')
            question_15b_desc = request.POST.get('question_15b_desc')
            question_15c = request.POST.get('question_15c')
            question_15c_desc = request.POST.get('question_15c_desc')

            respondent_county = request.POST.get('respondent_county')
            respondent_age = request.POST.get('respondent_age')
            respondent_race = request.POST.get('respondent_race')
            respondent_sex = request.POST.get('respondent_sex')
            respondent_ssn = request.POST.get('respondent_ssn')
            respondent_height = request.POST.get('respondent_height')
            respondent_weight = request.POST.get('respondent_weight')
            respondent_haircolor = request.POST.get('respondent_haircolor')
            respondent_eyecolor = request.POST.get('respondent_eyecolor')

            question_16 = request.POST.get('question_16')
            question_16_desc = request.POST.get('question_16_desc')
            question_17 = request.POST.get('question_17_desc')
            question_17_desc = request.POST.get('question_17_desc')
            question_18 = request.POST.get('question_18')
            question_18_desc = request.POST.get('question_18_desc')
            question_19 = request.POST.get('question_19')
            question_19_desc = request.POST.get('question_19_desc')

            question_20 = request.POST.get('question_20')
            question_20_desc = request.POST.get('question_20_desc')
            question_21 = request.POST.get('question_21')
            question_22 = request.POST.get('question_22')
            question_23 = request.POST.get('question_23')
            guardian_name = request.POST.get('guardian_name')
            guardian_phone = request.POST.get('guardian_phone')
            guardian_address = request.POST.get('guardian_address')
            guardian_city = request.POST.get('guardian_city')
            guardian_state = request.POST.get('guardian_state')
            guardian_zip = request.POST.get('guardian_zip')

            physician_name = request.POST.get('physician_name')
            physician_phone = request.POST.get('physician_phone')




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

            address_text = '<font size=12> <style="justify"> 1. a. Petitioner \
                    lives at the following address: <br></br><br></br> \
                    &nbsp &nbsp &nbsp &nbsp %s, <br></br> &nbsp &nbsp &nbsp &nbsp %s, %s, %s <br></br><br></br>\
                    &nbsp &nbsp &nbsp &nbsp Phone: %s \
                    </style></font>' % (petitioner_address,
                                        petitioner_city,
                                        petitioner_state,
                                        petitioner_zip,
                                        petitioner_phone,
                                        )

            Complaint.append(Paragraph(address_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            address_text = '<font size=12> <style="justify"> &nbsp &nbsp b. The Person \
                    lives or may be found at the following address: <br></br><br></br> \
                    &nbsp &nbsp &nbsp &nbsp %s, %s, %s, %s <br></br><br></br>\
                    &nbsp &nbsp &nbsp &nbsp or at the following alternate address: <br></br><br></br>\
                    &nbsp &nbsp &nbsp &nbsp %s, %s, %s, %s <br></br><br></br>\
                    </style></font>' % (respondent_address,
                                        respondent_city,
                                        respondent_state,
                                        respondent_zip,
                                        respondent_address_alt,
                                        respondent_city_alt,
                                        respondent_state_alt,
                                        respondent_zip_alt,
                                        )

            Complaint.append(Paragraph(address_text, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            relationship = '<font size=12> <style="justify"> &nbsp &nbsp 2. I have \
                    the following relationship with the Person: <br></br><br></br> \
                    %s <br></br><br></br>\
                    </style></font>' % relationship


            Complaint.append(Paragraph(relationship, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            good_terms = '<font size=12> <style="justify"> &nbsp &nbsp 3. I am \
                    %s on good terms with the Person. <br></br><br></br> \
                     <br></br>%s<br></br>\
                    </style></font>' % (good_terms_choice, good_terms_describe)


            Complaint.append(Paragraph(good_terms, styles["Justify"]))
            Complaint.append(Spacer(1, 12))


            four = '<font size=12> <style="justify"> &nbsp 4. I or \
                    a family member %s previously made allegations to law \
                    enforcement involving this Person, such as domestic violence,\
                    trespassing, battery, child abuse or neglect, Baker Act, \
                    neighborhood disputes, etc.<br></br> \
                     <br></br>%s\
                    </style></font>' % (previous_allegation_p_choice, previous_allegation_p_describe)


            Complaint.append(Paragraph(four, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            five = '<font size=12> <style="justify"> &nbsp 5. The Person \
                    %s previously made allegations to law \
                    enforcement about me or my family, such as domestic violence,\
                    trespassing, battery, child abuse or neglect, Baker Act, \
                    neighborhood disputes, etc.<br></br> \
                     <br></br>%s\
                    </style></font>' % (previous_allegation_r_choice, previous_allegation_r_describe)


            Complaint.append(Paragraph(five, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            six = '<font size=12> <style="justify"> &nbsp 6. The Person \
                    %s previously (or currently) been involved in criminal or\
                    delinquency charges.\
                    <br></br> \
                    </style></font>' % previous_crim_choice


            Complaint.append(Paragraph(six, styles["Justify"]))
            Complaint.append(Spacer(1, 12))

            seven = '<font size=12> <style="justify"> &nbsp 7. %s\
                    <br></br><br></br> %s\
                    </style></font>' % (previous_court_case, previous_court_case_describe)


            Complaint.append(Paragraph(seven, styles["Justify"]))
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
        knowledge_sub_abuse_info = KnowledgeAboutPersonInfo(request.POST)
        identifying_info = IdentifyingInfo(request.POST)
        picture_form = PictureID(request.POST, request.FILES)
        violence_info = ViolenceInfo(request.POST)
        atty_guardian_info = AttyGuardianInfo(request.POST)

    return render(request,'fl-mental-health/marchman-act.html',
                    {'header_info': header_info,
                    'location_info': location_info,
                    'relationship_info': relationship_info,
                    'good_terms_info': good_terms_info,
                    'previous_allegations_info': previous_allegations_info,
                    'knowledge_sub_abuse_info': knowledge_sub_abuse_info,
                    'identifying_info': identifying_info,
                    'picture_form': picture_form,
                    'violence_info': violence_info,
                    'atty_guardian_info': atty_guardian_info,
                    })
