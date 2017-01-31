from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from fl_discrim_helper.form_folder.employment_form import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def employment_complaint(request):

    cx_employment_form = CxEmploymentForm(request)
    cx_other_per_form = OpEmploymentForm(request)
    dis_employment_form = DisEmploymentForm(request)
    rep_employment_form = RepEmploymentForm(request)
    dis_employment_num_form = DisEmploymentNumForm(request)
    dis_employment_data_form = DisEmploymentDataForm(request)
    dis_reason_employment_form = DisReasonEmploymentForm(request)
    describe_employment_form = DescribeEmploymentForm(request)
    disability_ynm_form = DisabilityYNM(request)
    prior_agency_help = PriorComplaint(request)
    prior_sought_help = PriorSoughtHelp(request)
    box_1_2 = Box_1_2(request)

    if request.method == 'POST':

        cx_employment_form = CxEmploymentForm(request.POST)
        cx_other_per_form = OpEmploymentForm(request.POST)
        dis_employment_form = DisEmploymentForm(request.POST)
        rep_employment_form = RepEmploymentForm(request.POST)
        dis_employment_num_form = DisEmploymentNumForm(request.POST)
        dis_employment_data_form = DisEmploymentDataForm(request.POST)
        dis_reason_employment_form = DisReasonEmploymentForm(request.POST)
        describe_employment_form = DescribeEmploymentForm(request.POST)
        disability_ynm_form = DisabilityYNM(request.POST)
        prior_agency_help = PriorComplaint(request.POST)
        prior_sought_help = PriorSoughtHelp(request.POST)
        box_1_2 = Box_1_2(request.POST)

        if cx_employment_form.is_valid():
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

            disorg_type = request.POST.get('disorg_type')
            disorg_name = request.POST.get('disorg_name')
            disorg_street_address = request.POST.get('disorg_street_address')
            disorg_city = request.POST.get('disorg_city')
            disorg_county = request.POST.get('disorg_county')
            disorg_state = request.POST.get('disorg_state')
            disorg_zip = request.POST.get('disorg_zip')
            disorg_phone = request.POST.get('disorg_phone')
            disorg_type_biz = request.POST.get('disorg_type_biz')
            disorg_hr_dir = request.POST.get('disorg_hr_dir')
            disorg_hr_dir_phone = request.POST.get('disorg_hr_dir_phone')

            reporg_name = request.POST.get('reporg_name')
            reporg_street_address = request.POST.get('reporg_street_address')
            reporg_city = request.POST.get('reporg_city')
            reporg_county = request.POST.get('reporg_county')
            reporg_state = request.POST.get('reporg_state')
            reporg_zip = request.POST.get('reporg_zip')
            reporg_phone = request.POST.get('reporg_phone')

            employee_number_choose = request.POST.get('employee_number_choose')

            date_hired = request.POST.get('date_hired')
            job_title_at_hire = request.POST.get('job_title_at_hire')
            job_title_at_discrim = request.POST.get('job_title_at_discrim')
            date_quit_discharge = request.POST.get('date_quit_discharge')
            supervisor = request.POST.get('supervisor')
            applicant_date = request.POST.get('applicant_date')
            applicant_title = request.POST.get('applicant_title')


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

            reason_marital = request.POST.get('reason_marital')
            if reason_marital == "on":
                reason_marital = "X"
            else:
                reason_marital = "_"
            reason_marital_choose = request.POST.get('reason_marital_choose')

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

            reason_age = request.POST.get('reason_age')
            if reason_age == "on":
                reason_age = "X"
            else:
                reason_age = "_"

            reason_age_choose = request.POST.get('reason_age_choose')

            reason_retaliation = request.POST.get('reason_retaliation')
            if reason_retaliation == "on":
                reason_retaliation = "X"
            else:
                reason_retaliation = "_"


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

            reason_genetic = request.POST.get('reason_genetic')
            if reason_genetic == "on":
                reason_genetic = "X"
            else:
                reason_genetic = "_"
            reason_genetic_choose = request.POST.get('reason_genetic_choose')

            reason_other = request.POST.get('reason_other')
            if reason_other == "on":
                reason_other = "X"
            else:
                reason_other = "_"
            reason_other_desc = request.POST.get('reason_other_desc')


            reason_description = request.POST.get('reason_description')

            disability_ynm = request.POST.get('disability_ynm')

            prior_complaint = request.POST.get('prior_complaint')
            prior_complaint_agency = request.POST.get('prior_complaint_agency')

            prior_help = request.POST.get('prior_help')
            prior_help_description = request.POST.get('prior_help_description')

            box_1 = request.POST.get('box_1')
            if box_1 == "on":
                box_1 = "X"
            else:
                box_1 = "_"
            box_2 = request.POST.get('box_2')
            if box_2 == "on":
                box_2 = "X"
            else:
                box_2 = "_"



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
                    Technical Assistance Questionnaire for Employment \
                    Complaints </b></style></font>'

            Complaint.append(Paragraph(ptext, styles["Center"]))
            Complaint.append(Spacer(1, 12))

            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            ptext = '<font size=12> The primary purpose of this questionnaire is \
            to solicit information about claims of employment discrimination, \
            determine whether the Florida Commission on Human Relations (FCHR) \
            has jurisdiction over those claims and provide charge filing counseling, \
            as appropriate.  Providing this information is voluntary, but failure \
            to do so may impede the Commission’s investigation of a charge.  \
            It is not mandatory that this form be used to provide the requested \
            information.  NOTE: The FCHR may disclose the information included on \
            this form to other state, local and federal agencies, as appropriate \
            or necessary to carry out the Commission’s functions, or if the FCHR \
            becomes aware of a civil or criminal law violation. If the FCHR accepts \
            this form as a charge, this form will be provided to the employer, \
            union or employment agency identified.  </font>'

            Complaint.append(Paragraph(ptext, styles["Normal"]))
            Complaint.append(Spacer(1, 12))


            ptext = '<font size=12> Please complete this entire form (please print) \
            and return it to the Commission at the address listed at the bottom of \
            this form.  Answer all questions completely.  Attach additional pages, \
            if needed, to complete your responses. If you do not know the answer \
            to a question, answer by stating “not known.” If a question is not \
            applicable, write “N/A.”  </font>'

            Complaint.append(Paragraph(ptext, styles["Normal"]))
            Complaint.append(Spacer(1, 12))

            ptext = '<font size=12><b>REMEMBER, a charge of employment \
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

            name_info = '<font size=12><b>3. Please provide the name of a person we can \
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

            name_info = '<font size=12><b>3. I believe that I was discriminated against by:</b><br></br> <br></br> \
                    <b>Organization Type:</b> %s \
                    </font>' % disorg_type

            Complaint.append(Paragraph(name_info, styles["Normal"]))

            address_info = '<font size=12><b>Organization Contact Information:</b><br></br>\
                    <b>Organization Name: </b> %s <br></br>\
                    <b>Street or Mailing Address:</b> %s <br></br> \
                    <b>City: </b> %s <br></br> \
                    <b>County:</b> %s <br></br><b>State:</b> %s <br></br>\
                    <b>ZIP Code:</b> %s<br></br>\
                    <b>Telephone Number:</b> %s <br></br>\
                    <b>This person / entity is a:</b> %s <br></br>\
                    <b>Human Resources Director / Owner Name:</b> %s <br></br>\
                    <b>PR:</b> %s <br></br>\
                    </font>' % (disorg_name,
                                disorg_street_address,
                                disorg_city,
                                disorg_county,
                                disorg_state,
                                disorg_zip,
                                disorg_phone,
                                disorg_type_biz,
                                disorg_hr_dir,
                                disorg_hr_dir_phone,
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

            ### MORE THAN 15 EMPLOYEES? ###

            emp_num_info = '<font size=12><b>5. Does the Organization Employ 15 \
                    or More Employees?</b><br></br> <br></br> \
                    <b>Answer:</b> %s \
                    </font>' % employee_number_choose

            Complaint.append(Paragraph(emp_num_info, styles["Normal"]))
            Complaint.append(Spacer(1, 24))
            ### EMPLOYMENT DATA: ###

            emp_data_info = '<font size=12><b>6. Your employment data: \
                    </b><br></br> <br></br> \
                    <b>Date hired:</b> %s  <br></br> \
                    <b>Job title at hire:</b> %s  <br></br> \
                    <b>Job title at time of alleged discrimination:</b> %s  <br></br> \
                    <b>Date quit / discharged:</b> %s  <br></br> \
                    <b>Name and title of immediate supervisor:</b> %s  <br></br> \
                    <b>If job applicant, date applied for job:</b> %s  <br></br> \
                    <b>Job title applied for:</b> %s  <br></br> \
                    </font>' % (date_hired,
                                job_title_at_hire,
                                job_title_at_discrim,
                                date_quit_discharge,
                                supervisor,
                                applicant_date,
                                applicant_title,
                                )

            Complaint.append(Paragraph(emp_data_info, styles["Normal"]))

            ### DISCRIMINATION REASONS ###

            description = '<font size=12><b>7. What is the reason (basis) for your claim of \
                    employment discrimination? </b>  <br></br> <br></br>\
                    %s <b>Race:</b> %s  <br></br><br></br>\
                    %s <b>Color:</b> %s  <br></br><br></br>\
                    %s <b>National Origin:</b> %s  <br></br><br></br>\
                    %s <b>Marital Status:</b> %s  <br></br><br></br>\
                    %s <b>Sex:</b> %s  <br></br><br></br>\
                    %s <b>Pregnant or condition related to pregnancy or childbirth:</b><br></br><br></br>\
                    %s <b>Age:</b> %s  <br></br><br></br>\
                    %s <b>Retaliation</b> <br></br><br></br>\
                    %s <b>Religion:</b> %s  <br></br><br></br>\
                    %s <b>Disability/Handicap:</b> %s  <br></br><br></br>\
                    %s <b>Genetic Information:</b> %s  <br></br><br></br>\
                    %s <b>Other Reason:</b> %s  <br></br><br></br>\
                    </font>' % (reason_race,
                                reason_race_choose,
                                reason_color,
                                reason_color_choose,
                                reason_natorigin,
                                reason_natorigin_choose,
                                reason_marital,
                                reason_marital_choose,
                                reason_sex,
                                reason_sex_choose,
                                reason_preg,
                                reason_age,
                                reason_age_choose,
                                reason_retaliation,
                                reason_religion,
                                reason_religion_desc,
                                reason_disability,
                                reason_disability_choose,
                                reason_genetic,
                                reason_genetic_choose,
                                reason_other,
                                reason_other_desc,

                                )

            Complaint.append(Paragraph(description, styles["Normal"]))


            ### Description ###

            description_info = '<font size=12><b>8. What happened to you that you believe was \
                    discriminatory? Include the date(s) of harm, the action(s), and the \
                    name(s) and title(s) of the person(s) who you believe discriminated \
                    against you. Please attach additional pages if needed.  \
                    (Example: 08/08/2011 – Discharged by Mr. John Smith, supervisor):\
                    </b><br></br> <br></br> \
                    %s \
                    <br></br> <br></br> \
                    </font>' % reason_description

            Complaint.append(Paragraph(description_info, styles["Normal"]))


            ### DISABILITY? ###

            disability_info = '<font size=12><b>9. Do you have a disability, \
                        which is a physical or mental impairment that substantially \
                        limits a major life activity, such as caring for yourself, \
                        performing manual tasks, walking, seeing, hearing, speaking, \
                        breathing, learning, or working?  Please check all that apply: \
                        <br></br> <br></br> \
                        Answer:</b> %s \
                    <br></br> <br></br> \
                    </font>' % disability_ynm


            Complaint.append(Paragraph(disability_info, styles["Normal"]))


            ### PRIOR FILE? ###

            disab_info = '<font size=12><b>9.Have you filed a charge previously \
                        on this matter with the EEOC or another agency?\
                        <br></br> <br></br> \
                        Answer:</b> %s \
                    <br></br> <br></br> \
                    <b>If so, provide the name of the agency and the date of filing:</b> %s  \
                    <br></br> <br></br> \
                    </font>' % (prior_complaint, prior_complaint_agency)


            Complaint.append(Paragraph(disab_info, styles["Normal"]))

            ### PRIOR HELP? ###

            disab_info = '<font size=12><b>9. Have you sought help about this \
                        situation from an attorney, or other source?<br></br> <br></br> \
                        Answer:</b> %s \
                    <br></br> <br></br> \
                    <b>If so, provide the name of the organization or person you\
                    spoke with, the date, and the outsome if any:</b> %s  \
                    <br></br> <br></br> \
                    </font>' % (prior_help, prior_help_description)


            Complaint.append(Paragraph(disab_info, styles["Normal"]))

            ### BOX 1 or 2 ###

            boxes_12 = '<font size=12><b>Please check one of the boxes below to \
            tell us what you would like us to do with the information you are \
            providing on this questionnaire.  If you would like to file a charge \
            of employment discrimination, you must do so within 365 \
            days from the date you were allegedly discriminated against.  \
            If you do not file a charge of discrimination within the time limit, \
            you will lose your ability to file a charge.  If you would like more \
            information before filing a charge or you have concerns about the \
            FCHR notifying the employer, union or employment agency about your \
            charge, you may wish to check Box 1.  If you want to file a charge, \
            you should check Box 2.</b>\
            <br></br> <br></br> \
                        <b>Box 1:</b> %s I want to talk to an FCHR employee \
                        before deciding whether to file a charge.  I understand \
                        that by checking this box, I have not filed a charge with \
                        the FCHR.  I also understand that I could lose my ability \
                        to file a charge if I do not file in time. \
                        \
                    <br></br> <br></br> \
                    <b>Box 2:</b> %s I want to file a charge of discrimination, \
                    and I authorize the FCHR to look into the discrimination I \
                    described above.  I understand that the FCHR must give the \
                    organization that I accuse of discrimination information \
                    about the charge, including my name.  I also understand that \
                    the FCHR can only accept charges of discrimination based on \
                    race, religion, sex, pregnancy, national origin, disability, \
                    age, genetic information, or retaliation for opposing discrimination.\
                    <br></br> <br></br> \
                    </font>' % (box_1, box_2)


            Complaint.append(Paragraph(boxes_12, styles["Normal"]))

            ### sIGNATURE ###

            signature = '<font size=12><b>  NOTE: If you have checked Box 2 above, \
            and your case is already 350 days or more from the alleged \
            discrimination, the FCHR will accept this form as a charge if it \
            meets the elements of a charge. </b> \
            <br></br> <br></br> \
            <b>BY SIGNING BELOW, I VERIFY THAT I HAVE READ THE ABOVE INFORMATION \
            AND THE FACTS STATED ARE TRUE.</b> \
            <br></br> <br></br> \
            Signature: ______________________________       Date: _______________\
            <br></br> <br></br> \
            <b><center>Mail or Fax this form to:</center></b><br></br> \
	        Florida Commission on Human Relations <br></br> \
		4075 Esplanade Way, Suite 110 <br></br> \
		Tallahassee, Florida 32399-7020 <br></br> \
		Telephone (850) 488-7082 <br></br> \
        		Facsimile (850) 487-1007\
                    <br></br> <br></br> \
                    </font>'


            Complaint.append(Paragraph(signature, styles["Normal"]))





            doc.build(Complaint)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response

    else:
        cx_employment_form = CxEmploymentForm()
        cx_other_per_form = OpEmploymentForm()
        dis_employment_form = DisEmploymentForm()
        rep_employment_form = RepEmploymentForm()
        dis_employment_num_form = DisEmploymentNumForm()
        dis_employment_data_form = DisEmploymentDataForm()
        dis_reason_employment_form = DisReasonEmploymentForm()
        describe_employment_form = DescribeEmploymentForm()
        disability_ynm_form = DisabilityYNM()
        prior_agency_help = PriorComplaint()
        prior_sought_help = PriorSoughtHelp()
        box_1_2 = Box_1_2()


    return render(request,
                    'fl-discrim-helper/employment-complaint.html',
                    {'cx_employment_form': cx_employment_form,
                    'cx_other_per_form': cx_other_per_form,
                    'dis_employment_form': dis_employment_form,
                    'rep_employment_form': rep_employment_form,
                    'dis_employment_num_form': dis_employment_num_form,
                    'dis_employment_data_form': dis_employment_data_form,
                    'dis_reason_employment_form': dis_reason_employment_form,
                    'describe_employment_form': describe_employment_form,
                    'disability_ynm_form': disability_ynm_form,
                    'prior_agency_help': prior_agency_help,
                    'prior_sought_help': prior_sought_help,
                    'box_1_2': box_1_2,
                    }
                    )



#
