from django import forms
from fl_discrim_helper.form_choices import *

class CxHousingForm(forms.Form):


    cx_first_name = forms.CharField(label = 'First Name ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    cx_last_name = forms.CharField(label = 'Last Name ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    cx_mi = forms.CharField(label = 'Middle Initial ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '4'})
                                )

    cx_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    cx_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    cx_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    cx_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = True,
                                )

    cx_county = forms.CharField(label = 'County ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    cx_zip = forms.CharField(label = 'Zip Code ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
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
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )


    cx_sex = forms.ChoiceField(label = 'Your Sex ',
                                choices = SEX_CHOICES,
                                required = True,
                                )

class CxOtherOccForm(forms.Form):

    other_occupants = forms.CharField(label = 'Are there any children or \
                                                other occupants? If so, list \
                                                them here along with their \
                                                dates of birth:',
                                                required = False,
                                                widget= forms.Textarea(),)

class OpHousingForm(forms.Form):


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


class DisHousingForm(forms.Form):

    disorg_name = forms.CharField(label = 'Who or what company do you believe \
                                            discriminated against you?',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )


    disorg_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    disorg_apt_num = forms.CharField(label = 'Suite or Office Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    disorg_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
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
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    disorg_phone = forms.CharField(label = 'Phone ',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'REQUIRED',
                                })
                                )

    disorg_type = forms.ChoiceField(label = 'This person or company is a:',
                                required = False,
                                choices = HOUSING_ORG_CHOICES,
                                )

    disorg_other_type = forms.CharField(label = 'If you selected "Other" please \
                                describe:',
                                required = False,
                                widget = forms.TextInput()
                                )

class RepHousingForm(forms.Form):

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


class DisReasonHousingForm(forms.Form):

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

    reason_familial = forms.BooleanField(label = 'Familial Status ', required = False,)

    reason_familial_choose = forms.ChoiceField(label = 'Your Familial Status ', required = False,
                                            choices = FAM_STAT_CHOICES,
                                            )


    reason_sex = forms.BooleanField(label = 'Sex ', required = False,)



    reason_sex_choose = forms.ChoiceField(label = 'Your Sex', required = False,
                                            choices = SEX_CHOICES,
                                            )

    reason_retaliation = forms.BooleanField(label = 'Retaliation (for \
                                        exercising or encouraging another \
                                        person to exercise a right under the \
                                        Fair Housing Act) ', required = False,)

    reason_religion = forms.BooleanField(label = 'Religion ', required = False,)

    reason_religion_desc = forms.CharField(label = 'Your Religious Affiliation ', required = False,
                                widget = forms.TextInput(),
                                )

    reason_disability = forms.BooleanField(label = 'Disability ', required = False,)

    reason_disability_choose = forms.ChoiceField(label = 'Disability Type ', required = False,
                                            choices = DISABILITY_CHOICES,
                                            )



    reason_other = forms.BooleanField(label = 'Other Reason ', required = False,)

    reason_other_desc = forms.CharField(label = 'If You Checked Other, Please Describe ', required = False,
                                widget = forms.TextInput(),
                                )

class HousingPropType(forms.Form):

    housing_type_choose = forms.ChoiceField(label = 'Type of Property ', required = True,
                                                choices = HOUSING_TYPE_CHOICES,
                                                )
    housing_other_desc = forms.CharField(label = 'If You Checked Other, Please Describe ', required = False,
                                widget = forms.TextInput(),
                                )


class HousingAddress(forms.Form):
    housing_street_address = forms.CharField(label = 'Street Address ',
                                required = False,
                                widget = forms.TextInput()
                                )

    housing_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = False,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    housing_city = forms.CharField(label = 'City ', required = False,
                                widget = forms.TextInput()
                                )

    housing_state = forms.ChoiceField(label = 'State ', required = False,
                                choices = STATE_CHOICES,
                                )

    housing_county = forms.CharField(label = 'County ', required = False,
                                widget = forms.TextInput()
                                )

    housing_zip = forms.CharField(label = 'Zip Code ', required = False,
                                widget = forms.TextInput()
                                )

class OwnerLiveThere(forms.Form):

    owner_live_choose = forms.ChoiceField(label = '', required = True,
                                                choices = YNM_CHOICES,
                                                )

class DescribeHousingForm(forms.Form):


    reason_description = forms.CharField(label = '', required = False,
                                widget = forms.Textarea(),
                                )


class PriorComplaint(forms.Form):

    prior_complaint = forms.ChoiceField(label = 'Have you Filed a Charge \
                                                Previously on this Matter with \
                                                HUD or Another Agency?', required = True,
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
