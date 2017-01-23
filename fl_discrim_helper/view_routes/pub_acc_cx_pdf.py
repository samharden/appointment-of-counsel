
def pub_acc_cx_pdf(cx_last_name):
            import time
            from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from django.http import HttpResponse
            from django.core.files.storage import FileSystemStorage
            from reportlab.pdfgen import canvas
            from io import BytesIO
            from django.shortcuts import render, get_object_or_404
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s-complaint.pdf"' % cx_last_name
            buffer = BytesIO()
            # response['Content-Disposition'] = 'attachment; filename="filename.pdf"'
            doc = SimpleDocTemplate(buffer,
                                    pagesize=letter,
                                    rightMargin=72,leftMargin=72,
                                    topMargin=72,bottomMargin=50)
            Complaint=[]

            # cx_last_name = "Driscoll"
            cx_first_name = "Mike"
            cx_mi = "K"
            cx_street_address = "2345 Address Street"
            cx_apt_num = "NA"
            cx_city = "Gatorville"
            cx_county = "Hillsborough"
            cx_state = "FL"
            cx_zip = "33606"
            cx_phone = "(333)444-5555"
            cx_email = "Email@email.com"
            cx_dob = "11/22/33"
            cx_sex = "Male"

            op_last_name = "Driscoll"
            op_first_name = "Mike"
            op_mi = "K"
            op_relationship = "Me"
            op_street_address = "2345 Address Street"
            op_apt_num = "NA"
            op_city = "Gatorville"
            op_county = "Hillsborough"
            op_state = "FL"
            op_zip = "33606"
            op_phone = "(333)444-5555"

            disorg_name = "Bad Business"
            disorg_street_address = "54321 Organization Row"
            disorg_city = "Brandon"
            disorg_county = "Organge"
            disorg_state = "FL"
            disorg_zip = "98765"
            disorg_phone = "87238742"
            disorg_type = "Crack House"
            disorg_owner = "Bill Dance"
            disorg_owner_phone = "666 666 666"

            reporg_name = "Getyy"
            reporg_street_address = "ghfgh"
            reporg_city = "khfkjfhjhf"
            reporg_county = "7rfjhfjf"
            reporg_state = "hiufjg"
            reporg_zip = "ugtfjhfjh"
            reporg_phone = "08979087"

            reason_race = "race"
            reason_race_choose = "white"
            reason_color = "color"
            reason_color_choose = "light"
            reason_natorigin = "nat origin"
            reason_natorigin_choose = "american"
            reason_sex = "Sex"
            reason_sex_choose = "male"
            reason_preg = "preg"
            reason_religion = "religion"
            reason_religion_desc = "athiest"
            reason_disability = "disabili8tuy"
            reason_disability_choose = "cant ttype"
            reason_familial = "family"
            reason_familial_desc = "married"
            reason_other = "other"
            reason_other_desc = "none"

            reason_description = """
            Ramps DIY vaporware intelligentsia. Seitan letterpress la croix, echo park \
            intelligentsia farm-to-table yuccie ramps tbh quinoa prism iceland poke VHS \
            enamel pin. Ennui beard tumblr, kogi stumptown disrupt drinking vinegar \
            sustainable synth iceland poke wayfarers vexillologist affogato mlkshk. \
            Dreamcatcher hella brunch tote bag, thundercats actually franzen. Vice hell \
            of you probably haven't heard of them sartorial, sustainable wolf bicycle \
            rights forage direct trade aesthetic ugh pok pok PBR&B narwhal mustache. \
            Before they sold out poke vexillologist master cleanse DIY occupy. Tumblr \
            viral kickstarter +1.
            """

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
                    %s <b>Race:</b> %s  <br></br>\
                    %s <b>Color:</b> %s  <br></br>\
                    %s <b>National Origin:</b> %s  <br></br>\
                    %s <b>Sex:</b> %s  <br></br>\
                    %s <b>Pregnant or Condition Related to Pregnancy or Childbirth</b>  <br></br>\
                    %s <b>Religion:</b> %s  <br></br>\
                    %s <b>Disability/Handicap:</b> %s  <br></br>\
                    %s <b>Familial Status:</b> %s  <br></br>\
                    %s <b>Other Reason:</b> %s  <br></br>\
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

                    # response = HttpResponse(content_type='application/pdf')
                    # response['Content-Disposition'] = 'attachment; filename="filename.pdf"'
                    #
                    # # p = canvas.Canvas(response)
                    # # p.drawString(100, 800, cx_first_name)
                    # #
                    # # p.showPage()
                    # # p.save()


            doc.build(Complaint)



            # from fl_discrim_helper.view_routes.pub_acc_cx_pdf import pub_acc_cx_pdf
            # pub_acc_cx_pdf(cx_last_name)


            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)



            # print(response)
            # # buff = StringIO()
            # # response.write(pdf)
            # buff.close()

            return response

    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="%s-complaint.pdf"' % cx_last_name
    # buff = StringIO()
    # # response.write(pdf)
    # buff.close()
    #
    # return response

    # return pdf




    # # return pdf
    # pdf = doc.build(Complaint)
    # response = HttpResponse(pdf, content_type='application/pdf')
    # buff = StringIO()
    # response.write(pdf)
    # buff.close()
    # return response


    # # pdf = doc.build(Complaint)
    # # response.write(pdf)
