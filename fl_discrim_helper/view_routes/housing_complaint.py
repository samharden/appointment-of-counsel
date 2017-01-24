from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from fl_discrim_helper.form_folder.pub_acc_complaint_form import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def housing_complaint(request):

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

            cx_last_name = request.POST.get('cx_last_name')

            cx_first_name = request.POST.get('cx_first_name')
            cx_mi = request.POST.get('cx_mi')
            cx_street_address = request.POST.get('cx_street_address')
            cx_apt_num = request.POST.get('cx_apt_num')
            cx_city = request.POST.get('cx_city')
            cx_county = request.POST.get('cx_county')
            cx_state = request.POST.get('cx_state')
            cx_zip = request.POST.get('cx_zip')
            cx_phone = request.POST.get('cx_phone')
            cx_email = request.POST.get('cx_email')
            cx_dob = request.POST.get('cx_dob')
            cx_sex = request.POST.get('cx_sex')

            op_last_name = request.POST.get('op_last_name')
            op_first_name = request.POST.get('op_first_name')
            op_mi = request.POST.get('op_mi')
            op_relationship = request.POST.get('op_relationship')
            op_street_address = request.POST.get('op_street_address')
            op_apt_num = request.POST.get('op_apt_num')
            op_city = request.POST.get('op_city')
            op_county = request.POST.get('op_county')
            op_state = request.POST.get('op_state')
            op_zip = request.POST.get('op_zip')
            op_phone = request.POST.get('op_phone')

            disorg_name = request.POST.get('disorg_name')
            disorg_street_address = request.POST.get('disorg_street_address')
            disorg_city = request.POST.get('disorg_city')
            disorg_county = request.POST.get('disorg_county')
            disorg_state = request.POST.get('disorg_state')
            disorg_zip = request.POST.get('disorg_zip')
            disorg_phone = request.POST.get('disorg_phone')
            disorg_type = request.POST.get('disorg_type')
            disorg_owner = request.POST.get('disorg_owner')
            disorg_owner_phone = request.POST.get('disorg_owner_phone')

            reporg_name = request.POST.get('reporg_name')
            reporg_street_address = request.POST.get('reporg_street_address')
            reporg_city = request.POST.get('reporg_city')
            reporg_county = request.POST.get('reporg_county')
            reporg_state = request.POST.get('reporg_state')
            reporg_zip = request.POST.get('reporg_zip')
            reporg_phone = request.POST.get('reporg_phone')

            reason_race = request.POST.get('reason_race')
            if reason_race == "on":
                reason_race = "X"
            else:
                reason_race = "_"
            reason_race_choose = request.POST.get('reason_race_choose')

            reason_color = request.POST.get('reason_color')
            if reason_color == "on":
                reason_color = "X"
            else:
                reason_color = "_"
            reason_color_choose = request.POST.get('reason_color_choose')

            reason_natorigin = request.POST.get('reason_natorigin')
            if reason_natorigin == "on":
                reason_natorigin = "X"
            else:
                reason_natorigin = "_"
            reason_natorigin_choose = request.POST.get('reason_natorigin_choose')

            reason_sex = request.POST.get('reason_sex')
            if reason_sex == "on":
                reason_sex = "X"
            else:
                reason_sex = "_"
            reason_sex_choose = request.POST.get('reason_sex_choose')

            reason_preg = request.POST.get('reason_preg')
            if reason_preg == "on":
                reason_preg = "X"
            else:
                reason_preg = "_"

            reason_religion = request.POST.get('reason_religion')
            if reason_religion == "on":
                reason_religion = "X"
            else:
                reason_religion = "_"
            reason_religion_desc = request.POST.get('reason_religion_desc')

            reason_disability = request.POST.get('reason_disability')
            if reason_disability == "on":
                reason_disability = "X"
            else:
                reason_disability = "_"
            reason_disability_choose = request.POST.get('reason_disability_choose')

            reason_familial = request.POST.get('reason_familial')
            if reason_familial == "on":
                reason_familial = "X"
            else:
                reason_familial = "_"
            reason_familial_desc = request.POST.get('reason_familial_desc')

            reason_other = request.POST.get('reason_other')
            if reason_other == "on":
                reason_other = "X"
            else:
                reason_other = "_"
            reason_other_desc = request.POST.get('reason_other_desc')

            reason_description = request.POST.get('reason_description')

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s-complaint.pdf"' % cx_last_name
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer,
                                    pagesize=letter,
                                    rightMargin=72,leftMargin=72,
                                    topMargin=72,bottomMargin=50)
            Complaint=[]

            styles=getSampleStyleSheet()

            ### INTRO TEXT ###

            styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
            ptext = '<font size=14> <style="center"> <b>Florida Commission on Human Relations \
                    Technical Assistance Questionnaire for Public Accommodation \
                    Complaints </b></style></font>'

            Complaint.append(Paragraph(ptext, styles["Center"]))
            Complaint.append(Spacer(1, 12))

            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            ptext = '<font size=12>Please complete this entire form please print) and \
                    return it to the Commission at the address listed at the bottom of \
                    this form.  Answer all questions completely.  Attac <br></br>h additional pages \
                    if needed to complete your responses. If you do not know the answer to \
                    a question, answer by stating “not known.” If a question is not \
                    applicable, write “N/A.”</font>'

            Complaint.append(Paragraph(ptext, styles["Normal"]))
            Complaint.append(Spacer(1, 12))

            ptext = '<font size=12><b>REMEMBER, a charge of public accommodation \
                    discrimination must be filed within 365 days of the alleged act of \
                    discrimination.</b></font>'

            Complaint.append(Paragraph(ptext, styles["Normal"]))
            Complaint.append(Spacer(1, 12))

            ### PERSONAL INFORMATION ###

            name_info = '<font size=12><b>1. Personal Information: </b><br></br> <br></br> \
                    <b>Last Name:</b> %s <b>First Name: </b> %s <b>MI:</b> %s\
                    </font>' % (cx_last_name, cx_first_name, cx_mi)

            Complaint.append(Paragraph(name_info, styles["Normal"]))

            address_info = '<font size=12><b>Street or Mailing Address:</b> %s <br></br> \
                    <b>Apt. or Unit No.:</b> %s <br></br><b>City: </b> %s <br></br \
                    ><b>County:</b> %s <br></br><b>State:</b> %s <br></br>\
                    <b>ZIP Code:</b> %s<br></br>\
                    <b>Telephone Number:</b> %s <br></br>\
                    <b>Date of Birth:</b> %s <br></br>\
                    <b>Email Address:</b> %s <br></br>\
                    <b>Sex:</b> %s <br></br>\
                    \
                    \
                    </font>' % (cx_street_address,
                                cx_apt_num,
                                cx_city,
                                cx_county,
                                cx_state,
                                cx_zip,
                                cx_phone,
                                cx_dob,
                                cx_email,
                                cx_sex
                                )

            Complaint.append(Paragraph(address_info, styles["Normal"]))
            Complaint.append(Spacer(1, 24))

            ### OTHER CONTACT INFORMATION ###

            name_info = '<font size=12><b>2. Please provide the name of a person we can \
                    contact if we are unable to reach you: </b><br></br> <br></br> \
                    <b>Last Name:</b> %s <b>First Name: </b> %s <b>MI:</b> %s\
                    <b>Relationship:</b> %s\
                    </font>' % (op_last_name,
                                                op_first_name,
                                                op_mi,
                                                op_relationship)

            Complaint.append(Paragraph(name_info, styles["Normal"]))

            address_info = '<font size=12><b>Street or Mailing Address:</b> %s <br></br> \
                    <b>Apt. or Unit No.:</b> %s <br></br><b>City: </b> %s <br></br \
                    ><b>County:</b> %s <br></br><b>State:</b> %s <br></br>\
                    <b>ZIP Code:</b> %s<br></br>\
                    <b>Telephone Number:</b> %s <br></br>\
                    </font>' % (op_street_address,
                                op_apt_num,
                                op_city,
                                op_county,
                                op_state,
                                op_zip,
                                op_phone,
                                )

            Complaint.append(Paragraph(address_info, styles["Normal"]))
            Complaint.append(Spacer(1, 24))

            ### DISCRIMINATING ORGANIZATION ###

            name_info = '<font size=12><b>3. I believe that I was discriminated against by \
                    the following organization(s):</b><br></br> <br></br> \
                    <b>Organization Name:</b> %s \
                    </font>' % disorg_name

            Complaint.append(Paragraph(name_info, styles["Normal"]))

            address_info = '<font size=12><b>Street or Mailing Address:</b> %s <br></br> \
                    <b>City: </b> %s <br></br \
                    ><b>County:</b> %s <br></br><b>State:</b> %s <br></br>\
                    <b>ZIP Code:</b> %s<br></br>\
                    <b>Telephone Number:</b> %s <br></br>\
                    <b>Type of Business:</b> %s <br></br>\
                    <b>Owner Name:</b> %s <br></br>\
                    <b>Owner Telephone:</b> %s <br></br>\
                    </font>' % (disorg_street_address,
                                disorg_city,
                                disorg_county,
                                disorg_state,
                                disorg_zip,
                                disorg_phone,
                                disorg_type,
                                disorg_owner,
                                disorg_owner_phone,
                                )

            Complaint.append(Paragraph(address_info, styles["Normal"]))
            Complaint.append(Spacer(1, 24))

            ### DISCRIMINATING ORGANIZATION REP CONTACT ###

            name_info = '<font size=12><b>4. Organization Representative Contact \
                    Information (If known):</b><br></br> <br></br> \
                    <b>Representative Name:</b> %s \
                    </font>' % reporg_name

            Complaint.append(Paragraph(name_info, styles["Normal"]))

            address_info = '<font size=12><b>Street or Mailing Address:</b> %s <br></br> \
                    <b>City: </b> %s <br></br \
                    ><b>County:</b> %s <br></br><b>State:</b> %s <br></br>\
                    <b>ZIP Code:</b> %s<br></br>\
                    <b>Telephone Number:</b> %s <br></br>\
                    </font>' % (reporg_street_address,
                                reporg_city,
                                reporg_county,
                                reporg_state,
                                reporg_zip,
                                reporg_phone,
                                )

            Complaint.append(Paragraph(address_info, styles["Normal"]))
            Complaint.append(Spacer(1, 24))

            ### DISCRIMINATION REASONS ###

            description = '<font size=12><b>5. What is the reason (basis) for your claim of \
                    public accommodations discrimination? </b>  <br></br> <br></br>\
                    %s <b>Race:</b> %s  <br></br><br></br>\
                    %s <b>Color:</b> %s  <br></br><br></br>\
                    %s <b>National Origin:</b> %s  <br></br><br></br>\
                    %s <b>Sex:</b> %s  <br></br><br></br>\
                    %s <b>Pregnant or Condition Related to Pregnancy or Childbirth</b>  <br></br><br></br>\
                    %s <b>Religion:</b> %s  <br></br><br></br>\
                    %s <b>Disability/Handicap:</b> %s  <br></br><br></br>\
                    %s <b>Familial Status:</b> %s  <br></br><br></br>\
                    %s <b>Other Reason:</b> %s  <br></br><br></br>\
                    </font>' % (reason_race,
                                reason_race_choose,
                                reason_color,
                                reason_color_choose,
                                reason_natorigin,
                                reason_natorigin_choose,
                                reason_sex,
                                reason_sex_choose,
                                reason_preg,
                                reason_religion,
                                reason_religion_desc,
                                reason_disability,
                                reason_disability_choose,
                                reason_familial,
                                reason_familial_desc,
                                reason_other,
                                reason_other_desc,

                                )

            Complaint.append(Paragraph(description, styles["Normal"]))

            ### DISCRIMINATING ORGANIZATION REP CONTACT ###

            name_info = '<font size=12><b>6. What happened to you that you believe was \
                    discriminatory? Include the date(s) of harm, the action(s), and the \
                    name(s) and title(s) of the person(s) who you believe discriminated \
                    against you. Please attach additional pages if needed.  \
                    (Example: 08/08/2011 – Refused service by Mr. John Smith, waiter):\
                    </b><br></br> <br></br> \
                    %s \
                    </font>' % reason_description

            Complaint.append(Paragraph(name_info, styles["Normal"]))
            doc.build(Complaint)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response

    else:
        cx_pub_acc_form = CxPubAccForm()
        op_pub_acc_form = OpPubAccForm()
        disorg_pub_acc_form = DisOrgPubAccForm()
        reporg_pub_acc_form = RepOrgPubAccForm()
        disreason_pub_acc_form = DisReasonPubAccForm()


    return render(request,
                    'fl-discrim-helper/housing-complaint.html',
                    {'cx_pub_acc_form': cx_pub_acc_form,
                    'op_pub_acc_form': op_pub_acc_form,
                    'disorg_pub_acc_form': disorg_pub_acc_form,
                    'reporg_pub_acc_form': reporg_pub_acc_form,
                    'disreason_pub_acc_form': disreason_pub_acc_form,
                    }
                    )



#
