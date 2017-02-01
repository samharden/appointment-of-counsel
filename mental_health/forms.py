
from django import forms
from mental_health.form_choices import *


#

class MentalIndexForm(forms.Form):
    choice = forms.ChoiceField(label = '',
                                        choices = INDEX_CHOICES,
                                        required = False,

                                        )
