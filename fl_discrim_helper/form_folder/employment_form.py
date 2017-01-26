from django import forms
from fl_discrim_helper.form_choices import *

class CxEmploymentForm(forms.Form):


    cx_first_name = forms.CharField(label = 'First Name ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_last_name = forms.CharField(label = 'Last Name ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_mi = forms.CharField(label = 'Middle Initial ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '4'})
                                )

    cx_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    cx_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = True,
                                )

    cx_county = forms.CharField(label = 'County ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_zip = forms.CharField(label = 'Zip Code ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_phone = forms.CharField(label = 'Phone ',
                                required = False,
                                widget = forms.TextInput()
                                )

    cx_email = forms.CharField(label = 'Email ',
                                required = False,
                                widget = forms.TextInput()
                                )

    cx_dob = forms.CharField(label = 'Date of Birth',
                                required = True,
                                widget = forms.TextInput()
                                )


    cx_sex = forms.ChoiceField(label = 'Your Sex ',
                                choices = SEX_CHOICES,
                                required = True,
                                )


class OpEmploymentForm(forms.Form):


    op_first_name = forms.CharField(label = 'First Name ',
                                required = False,
                                widget = forms.TextInput()
                                )

    op_last_name = forms.CharField(label = 'Last Name ',
                                required = False,
                                widget = forms.TextInput()
                                )

    op_mi = forms.CharField(label = 'Middle Initial ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '4'})
                                )

    op_relationship = forms.CharField(label = 'Relationship',
                                        required = False,
                                        widget = forms.TextInput()
                                        )

    op_street_address = forms.CharField(label = 'Street Address ',
                                required = False,
                                widget = forms.TextInput()
                                )

    op_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    op_city = forms.CharField(label = 'City ',
                                required = False,
                                widget = forms.TextInput()
                                )

    op_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    op_zip = forms.CharField(label = 'Zip Code ',
                                required = False,
                                widget = forms.TextInput()
                                )

    op_phone = forms.CharField(label = 'Phone ',
                                required = False,
                                widget = forms.TextInput()
                                )


class DisEmploymentForm(forms.Form):

    disorg_type = forms.ChoiceField(label = '',
                                    choices = EMPLOYER_TYPE_CHOICES,
                                    required = False,
                                    )

    disorg_other_type = forms.CharField(label = 'If you selected "Other" please \
                                describe:',
                                required = False,
                                widget = forms.TextInput()
                                )

    disorg_name = forms.CharField(label = 'Organization Name:',
                                required = True,
                                widget = forms.TextInput()
                                )


    disorg_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    disorg_apt_num = forms.CharField(label = 'Suite or Office Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    disorg_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    disorg_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = True,
                                )

    disporg_county = forms.CharField(label = 'County ', required = False,
                                widget = forms.TextInput()
                                )

    disorg_zip = forms.CharField(label = 'Zip Code ',
                                required = True,
                                widget = forms.TextInput()
                                )

    disorg_phone = forms.CharField(label = 'Phone ',
                                required = True,
                                widget = forms.TextInput()
                                )

    disorg_type_biz = forms.CharField(label = 'Type of Business ',
                                required = True,
                                widget = forms.TextInput()
                                )
    disorg_hr_dir = forms.CharField(label = 'Human Resporces Director / Owner Name: ',
                                required = True,
                                widget = forms.TextInput()
                                )
    disorg_hr_dir_phone = forms.CharField(label = "HR Director or Owner's Phone: ",
                                required = True,
                                widget = forms.TextInput()
                                )


class RepEmploymentForm(forms.Form):

    reporg_name = forms.CharField(label = 'Representative Name ',
                                required = False,
                                widget = forms.TextInput()
                                )


    reporg_street_address = forms.CharField(label = 'Street Address ',
                                required = False,
                                widget = forms.TextInput()
                                )

    reporg_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    reporg_city = forms.CharField(label = 'City ', required = False,
                                widget = forms.TextInput()
                                )

    reporg_state = forms.ChoiceField(label = 'State ', required = False,
                                choices = STATE_CHOICES,
                                )

    reporg_county = forms.CharField(label = 'County ', required = False,
                                widget = forms.TextInput()
                                )

    reporg_zip = forms.CharField(label = 'Zip Code ', required = False,
                                widget = forms.TextInput()
                                )

    reporg_phone = forms.CharField(label = 'Phone ', required = False,
                                widget = forms.TextInput()
                                )


class DisEmploymentNumForm(forms.Form):

    employee_number_choose = forms.ChoiceField(label = '', required = True,
                                                choices = YNM_CHOICES,
                                                )

class DisEmploymentDataForm(forms.Form):

    date_hired = forms.CharField(label = 'Date Hired ', required = False,
                                widget = forms.TextInput()
                                )

    job_title_at_hire = forms.CharField(label = 'Job Title at Hire ', required = False,
                                widget = forms.TextInput()
                                )

    job_title_at_discrim = forms.CharField(label = 'Job Title at Time of Discrimination ', required = False,
                                widget = forms.TextInput()
                                )

    date_quit_discharge = forms.CharField(label = 'Date You Quit or Were Discharged ', required = False,
                                widget = forms.TextInput()
                                )

    supervisor = forms.CharField(label = 'Name and Title of Immediate Supervisor ', required = False,
                                widget = forms.TextInput()
                                )

    applicant_date = forms.CharField(label = 'If Job Applicant, the Date you Applied ',
                                required = False,
                                widget = forms.TextInput()
                                )

    applicant_title = forms.CharField(label = 'Job Title You Applied For ', required = False,
                                widget = forms.TextInput()
                                )

class DisReasonEmploymentForm(forms.Form):

    reason_race = forms.BooleanField(label = 'Race ', required = False,)

    reason_race_choose = forms.ChoiceField(label = 'Your Race', required = False,
                                            choices = RACE_CHOICES,
                                            )

    reason_color = forms.BooleanField(label = 'Color ', required = False,)

    reason_color_choose = forms.ChoiceField(label = 'Your Color', required = False,
                                            choices = COLOR_CHOICES,
                                            )

    reason_natorigin = forms.BooleanField(label = 'National Origin ', required = False,)

    reason_natorigin_choose = forms.ChoiceField(label = 'Your National Origin ', required = False,
                                            choices = NATORIGIN_CHOICES,
                                            )


    reason_marital = forms.BooleanField(label = 'Marital Status ', required = False,)

    reason_marital_choose = forms.ChoiceField(label = 'Your Marital Status ', required = False,
                                            choices = MARITAL_STAT_CHOICES,
                                            )


    reason_sex = forms.BooleanField(label = 'Sex ', required = False,)



    reason_sex_choose = forms.ChoiceField(label = 'Your Sex', required = False,
                                            choices = SEX_CHOICES,
                                            )

    reason_preg = forms.BooleanField(label = 'Pregnancy ', required = False,)


    reason_age = forms.BooleanField(label = 'Age ', required = False,)

    reason_age_choose = forms.ChoiceField(label = 'Your Age', required = False,
                                            choices = AGE_CHOICES,
                                            )

    reason_retaliation = forms.BooleanField(label = 'Retaliation', required = False,)

    reason_religion = forms.BooleanField(label = 'Religion ', required = False,)

    reason_religion_desc = forms.CharField(label = 'Your Religious Affiliation ', required = False,
                                widget = forms.TextInput(),
                                )

    reason_disability = forms.BooleanField(label = 'Disability ', required = False,)

    reason_disability_choose = forms.ChoiceField(label = 'Disability Type ', required = False,
                                            choices = DISABILITY_CHOICES,
                                            )

    reason_genetic = forms.BooleanField(label = 'Genetic ', required = False,)

    reason_genetic_choose = forms.ChoiceField(label = 'What Type of Genetic Information is Involved? ', required = False,
                                            choices = GENETIC_CHOICES,
                                            )




    reason_other = forms.BooleanField(label = 'Other Reason ', required = False,)

    reason_other_desc = forms.CharField(label = 'If You Checked Other, Please Describe ', required = False,
                                widget = forms.TextInput(),
                                )

class DescribeEmploymentForm(forms.Form):


    reason_description = forms.CharField(label = '', required = False,
                                widget = forms.Textarea(),
                                )

class DisabilityYNM(forms.Form):

    disability_ynm = forms.ChoiceField(label = '', choices = EMP_DISAB_YNM_CHOICES,
                                            required = False)

class PriorComplaint(forms.Form):

    prior_complaint = forms.ChoiceField(label = 'Have you Filed a Charge \
                                                Previously on this Matter with \
                                                the EEOC or Another Agency?', required = True,
                                                choices = YNM_CHOICES,
                                                )
    prior_complaint_agency = forms.CharField(label = 'If so, Please Provide the \
                                                    Name of the Agency and the \
                                                    Date of Filing', required = False,
                                widget = forms.TextInput()
                                )
class PriorSoughtHelp(forms.Form):

    prior_help = forms.ChoiceField(label = 'Have you Sought Help About this \
                                                Situation from an Attorney or \
                                                any Other Source?', required = True,
                                                choices = YNM_CHOICES,
                                                )
    prior_help_description = forms.CharField(label = 'If so, Please Provide the \
                                                    Name of the Organization, Date \
                                                    of Contact, and the Results or \
                                                    Outcome, if any:', required = False,
                                widget = forms.TextInput()
                                )

class Box_1_2(forms.Form):

    box_1 = forms.BooleanField(label = '', required = False,)

    box_2 = forms.BooleanField(label = '', required = False,)

    ###
