
from django import forms
from fl_discrim_helper.form_choices import *


#

class DiscrimIndexForm(forms.Form):
    choice = forms.ChoiceField(label = 'What would you like to do?',
                                        choices = INDEX_CHOICES,
                                        required = False,

                                        )

class DiscrimCaseTypeForm(forms.Form):
    case_type = forms.ChoiceField(label = 'Type of case:',
                                        choices = DISCRIM_CASETYPE_CHOICES,
                                        required = False,

                                        )
class complaintform(forms.Form):
    pass



class PubAccForm(forms.Form):
    state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = True,
                                )

    first_name = forms.CharField(label = 'First Name ',
                                required = True,
                                widget = forms.TextInput(
                                
                                )


                                )



class emp_disc(forms.Form):
    pass
