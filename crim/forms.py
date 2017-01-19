from django import forms
from crim.form_choices import *


#
class CrimCaseTypeForm(forms.Form):
    case_type = forms.ChoiceField(label = 'Type of case:',
                                        choices = CRIM_CASETYPE_CHOICES,
                                        required = False,

                                        )
    # state = forms.ChoiceField(label = 'State:',
    #                                 choices = CRIM_STATE_CHOICES,
    #                                 required = False,
    #
    #                                 )
    county = forms.ChoiceField(label = 'County:',
                                    choices = CRIM_COUNTY_CHOICES,
                                    required = False,

                                    )

class CrimDesc(forms.Form):
    crim_desc = forms.CharField(label = 'Describe what happened:',
                                    required = False,


                                    )

class PinellasJudges(forms.Form):
    pinell_judge = forms.ChoiceField(label = 'Judge',
                                    choices = CRIM_JUDGE_CHOICES_PINELL,
                                    required = False,

                                    )

class HillsboroughJudges(forms.Form):
    hillsb_judge = forms.ChoiceField(label = 'Judge',
                                    choices = CRIM_JUDGE_CHOICES_HILLSB,
                                    required = False,

                                    )
