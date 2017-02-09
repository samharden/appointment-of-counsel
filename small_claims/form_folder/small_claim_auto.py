from django import forms
from small_claims.form_choices import *

class HeaderInfo(forms.Form):

    county = forms.ChoiceField(label = 'County ',
                                choices = COUNTY_CHOICES,
                                required = True,
                                )

    respondent = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput()
                                )
    petitioner = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput()
                                )

    respondent_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    owner_name = forms.CharField(label = '',
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

    owner_address = forms.CharField(label = 'Street address ',
                                required = True,
                                widget = forms.TextInput()
                                )

    owner_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    owner_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    owner_zip = forms.CharField(label = 'Zip ',
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

    date_of_accident = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': 'i.e. May 31, 2015',
                                })
                                )

    city_of_accident = forms.CharField(label = '',
                                required = True,
                                widget = forms.TextInput(attrs={
                                'placeholder': '',
                                })
                                )

    physical_injuries = forms.ChoiceField(label = '',
                                choices = YN_CHOICES,
                                required = False,
                                )
