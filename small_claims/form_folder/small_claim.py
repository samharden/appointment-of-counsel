from django import forms
from small_claims.form_choices import *

class HeaderInfo(forms.Form):

    county = forms.ChoiceField(label = 'County ',
                                choices = COUNTY_CHOICES,
                                required = True,
                                )

    respondent = forms.CharField(label = 'Respondent ',
                                required = True,
                                widget = forms.TextInput()
                                )
    petitioner = forms.CharField(label = 'Petitioner ',
                                required = True,
                                widget = forms.TextInput()
                                )


class LocationInfo(forms.Form):


    petitioner_address = forms.CharField(label = 'Your street address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    petitioner_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    petitioner_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    petitioner_zip = forms.CharField(label = 'Zip ',
                                required = True,
                                widget = forms.TextInput()
                                )



    respondent_address = forms.CharField(label = 'Street address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    respondent_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    respondent_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    respondent_zip = forms.CharField(label = 'Zip ',
                                required = True,
                                widget = forms.TextInput()
                                )


class AmountInfo(forms.Form):
    amount = forms.CharField(label = 'Amount of money in damages you are seeking',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': '',
                                })
                                )

class DescriptionInfo(forms.Form):

    description = forms.CharField(label = 'Please explain what happened, being as specific as you can, and include the dates where possible.',
                                required = False,
                                widget = forms.Textarea()
                                )
