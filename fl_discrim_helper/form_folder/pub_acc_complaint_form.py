from django import forms
from fl_discrim_helper.form_choices import *

class CxPubAccForm(forms.Form):


    cx_first_name = forms.CharField(label = 'First Name ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_last_name = forms.CharField(label = 'Last Name ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_mi = forms.CharField(label = 'Middle Initial ',
                                required = True,
                                widget = forms.TextInput(attrs={'size': '4'})
                                )

    cx_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = True,
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
                                required = True,
                                widget = forms.TextInput()
                                )

    cx_email = forms.CharField(label = 'Email ',
                                required = True,
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

class OpPubAccForm(forms.Form):


    op_first_name = forms.CharField(label = 'First Name ',
                                required = True,
                                widget = forms.TextInput()
                                )

    op_last_name = forms.CharField(label = 'Last Name ',
                                required = True,
                                widget = forms.TextInput()
                                )

    op_mi = forms.CharField(label = 'Middle Initial ',
                                required = True,
                                widget = forms.TextInput(attrs={'size': '4'})
                                )

    op_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    op_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = True,
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    op_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    op_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = True,
                                )

    op_county = forms.CharField(label = 'County ',
                                required = True,
                                widget = forms.TextInput()
                                )

    op_zip = forms.CharField(label = 'Zip Code ',
                                required = True,
                                widget = forms.TextInput()
                                )

    op_phone = forms.CharField(label = 'Phone ',
                                required = True,
                                widget = forms.TextInput()
                                )


class DisOrgPubAccForm(forms.Form):

    disorg_name = forms.CharField(label = 'Organization Name ',
                                required = True,
                                widget = forms.TextInput()
                                )


    disorg_street_address = forms.CharField(label = 'Street Address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    disorg_apt_num = forms.CharField(label = 'Apartment Number ',
                                required = True,
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

    disorg_county = forms.CharField(label = 'County ',
                                required = True,
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

    disorg_owner = forms.CharField(label = 'Owner of Organization ',
                                required = True,
                                widget = forms.TextInput()
                                )

    disorg_owner_phone = forms.CharField(label = "Owner's Telephone " ,
                                required = True,
                                widget = forms.TextInput()
                                )

class RepOrgPubAccForm(forms.Form):

    reporg_name = forms.CharField(label = 'Last Name ',
                                widget = forms.TextInput()
                                )


    reporg_street_address = forms.CharField(label = 'Street Address ',
                                widget = forms.TextInput()
                                )

    reporg_apt_num = forms.CharField(label = 'Apartment Number ',
                                widget = forms.TextInput(attrs={'size': '6'})
                                )


    reporg_city = forms.CharField(label = 'City ',
                                widget = forms.TextInput()
                                )

    reporg_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                )

    reporg_county = forms.CharField(label = 'County ',
                                widget = forms.TextInput()
                                )

    reporg_zip = forms.CharField(label = 'Zip Code ',
                                widget = forms.TextInput()
                                )

    reporg_phone = forms.CharField(label = 'Phone ',
                                widget = forms.TextInput()
                                )


class DisReasonPubAccForm(forms.Form):

    reason_race = forms.BooleanField(label = 'Race ')

    reason_race_choose = forms.ChoiceField(label = 'Your Race',
                                            choices = RACE_CHOICES,
                                            )

    reason_color = forms.BooleanField(label = 'Color ')

    reason_color_choose = forms.ChoiceField(label = 'Your Color',
                                            choices = COLOR_CHOICES,
                                            )

    reason_natorigin = forms.BooleanField(label = 'National Origin ')

    reason_natorigin_choose = forms.ChoiceField(label = 'Your National Origin ',
                                            choices = NATORIGIN_CHOICES,
                                            )

    reason_sex = forms.BooleanField(label = 'Sex ')

    reason_sex_choose = forms.ChoiceField(label = 'Your Sex',
                                            choices = SEX_CHOICES,
                                            )

    reason_preg = forms.BooleanField(label = 'Pregnancy ')

    reason_religion = forms.BooleanField(label = 'Religion ')

    reason_religion_desc = forms.CharField(label = 'Your Religious Affiliation ',
                                widget = forms.TextInput(),
                                )

    reason_disability = forms.BooleanField(label = 'Disability ')

    reason_disability_choose = forms.ChoiceField(label = 'Disability Type ',
                                            choices = DISABILITY_CHOICES,
                                            )


    reason_description = forms.CharField(label = 'Please describe what happened:',
                                widget = forms.Textarea(),
                                )






    ###
