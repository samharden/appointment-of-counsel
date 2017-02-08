
from django import forms
from small_claims.form_choices import *


#

class SmallClaimsIndexForm(forms.Form):
    choice = forms.ChoiceField(label = '',
                                        choices = INDEX_CHOICES,
                                        required = False,

                                        )
