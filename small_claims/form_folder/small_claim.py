from django import forms
from mental_health.form_choices import *

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

    respondent_age_choose = forms.ChoiceField(label='Is the person 18 years of age or older? ',
                                        choices = YN_CHOICES,
                                        required = True,
                                        )

    respondent_age = forms.CharField(label = 'Their age (if known) ',
                                    required = False,
                                    widget = forms.TextInput(),
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

    respondent_address_alt = forms.CharField(label = 'Street address ',
                                required = False,
                                widget = forms.TextInput()
                                )

    respondent_city_alt = forms.CharField(label = 'City ',
                                required = False,
                                widget = forms.TextInput()
                                )

    respondent_state_alt = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    respondent_zip_alt = forms.CharField(label = 'Zip ',
                                required = False,
                                widget = forms.TextInput()
                                )

class RelationshipInfo(forms.Form):
    relationship = forms.CharField(label = 'I have the following relationship with the person ',
                                required = False,
                                widget = forms.TextInput()
                                )

class GoodTermsInfo(forms.Form):
    good_terms = forms.ChoiceField(label='Are you on good terms with the person? ',
                                        choices = YN_CHOICES,
                                        required = True,
                                        )
    good_terms_describe = forms.CharField(label = 'If you chose no, please explain:',
                                required = False,
                                widget = forms.Textarea()
                                )

class PreviousAllegationsInfo(forms.Form):
        previous_allegation = forms.ChoiceField(label='',
                                            choices = YN_CHOICES,
                                            required = True,
                                            )

        relationship = forms.CharField(label = '',
                                required = False,
                                widget = forms.TextInput()
                                )

class KnowledgeAboutPersonInfo(forms.Form):
    pass

class IdentifyingInfo(forms.Form):
    race = forms.BooleanField(label = 'Race ', required = False,)
