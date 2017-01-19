from django import forms
from main.form_choices import *

class LoginForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length=40, required=True)
    password = forms.CharField(label = 'Password', max_length=40, required=True)
#
class ProblemForm(forms.Form):
    case_type = forms.ChoiceField(label = '',
                                        choices = CASETYPE_CHOICES,
                                        required = True,

                                        )
    state = forms.ChoiceField(label = 'State',
                                        choices = STATE_CHOICES,
                                        required = True,
                                        )
