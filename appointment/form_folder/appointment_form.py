from django import forms
from appointment.form_choices import *

class FormInfo(forms.Form):

    county = forms.ChoiceField(label = 'County ',
                                choices = COUNTY_CHOICES,
                                required = True,
                                )

    defendant_name = forms.CharField(label = 'Defendant Name',
                                required = True,
                                widget = forms.TextInput()
                                )
    case_no = forms.CharField(label = 'Case Numbers ',
                                required = True,
                                widget = forms.TextInput()
                                )


    charges = forms.CharField(label = 'Charges ',
                                required = True,
                                widget = forms.TextInput()
                                )



    judge = forms.ChoiceField(label = 'Judge ',
                                choices = JUDGE_CHOICES,
                                required = False,
                                )
    hearing_date = forms.CharField(label = 'Hearing Date',
                                required = True,
                                widget = forms.TextInput()
                                )
