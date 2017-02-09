
from django import forms
from small_claims.form_choices import *


#

class SmallClaimsIndexForm(forms.Form):
    choice = forms.ChoiceField(label = '',
                                        choices = INDEX_CHOICES,
                                        required = False,

                                        )

class SmallClaimsComplaintChoiceForm(forms.Form):
    choice = forms.ChoiceField(label = '',
                                        choices = COMPLAINT_TYPE_CHOICES,
                                        required = False,

                                        )
class SmallClaimsAutoComplaintChoiceForm(forms.Form):
    choice = forms.ChoiceField(label = '',
                                        choices = YN_CHOICES,
                                        required = False,

                                        )
