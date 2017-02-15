from django import forms
from small_claims.form_choices import *

class CaseInfo(forms.Form):

    county = forms.ChoiceField(label = 'County ',
                                choices = COUNTY_CHOICES,
                                required = True,
                                )

    party_name = forms.CharField(label = '',
                                required = False,
                                widget = forms.TextInput()
                                )
    case_number = forms.CharField(label = '',
                            required = False,
                            widget = forms.TextInput()
                            )
