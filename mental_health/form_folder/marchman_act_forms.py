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

    petitioner_phone = forms.CharField(label = 'Phone ',
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
                                widget = forms.Textarea()
                                )

class GoodTermsInfo(forms.Form):
    good_terms = forms.ChoiceField(label='Are you on good terms with the person? ',
                                        choices = YN_CHOICES,
                                        required = False,
                                        )
    good_terms_describe = forms.CharField(label = 'If you chose no, please explain:',
                                required = False,
                                widget = forms.Textarea()
                                )

class PreviousAllegationsInfo(forms.Form):
        previous_allegation_p = forms.ChoiceField(label='Have you previously made \
                                            allegations to law enforcement \
                                            involving this Person, such as domestic \
                                            violence, trespassing, battery, \
                                            child abuse or neglect, Baker Act, \
                                            neighborhood disputes, etc. ',
                                            choices = YN_CHOICES,
                                            required = False,
                                            )

        previous_allegation_p_describe = forms.CharField(label = 'If you have, please describe ',
                                required = False,
                                widget = forms.TextInput()
                                )

        previous_allegation_r = forms.ChoiceField(label='Hase the Person made \
                                                    allegations to law enforcement \
                                                    against you or your family, such as domestic \
                                                    violence, trespassing, battery, \
                                                    child abuse or neglect, Baker Act, \
                                                    neighborhood disputes, etc. ',
                                            choices = YN_CHOICES,
                                            required = False,
                                            )

        previous_allegation_r_describe = forms.CharField(label = 'If they have, please describe ',
                                required = False,
                                widget = forms.TextInput()
                                )

        previous_crim = forms.ChoiceField(label='Has the person previously had \
                                        criminal or delinquency charges',
                                        choices = YN_CHOICES,
                                        required = False,
                                        )

        previous_court_case = forms.ChoiceField(label='Have you or a family member \
                                        been involved in a court case with the Person? ',
                                        choices = YN_CHOICES,
                                        required = False,
                                        )

        previous_court_case_describe = forms.CharField(label = 'If you have, please describe \
                                the type of case, the year, and what happened ',
                                required = False,
                                widget = forms.Textarea()
                                )

        how_long_known = forms.CharField(label = 'How long have you known the Person ',
                                required = False,
                                widget = forms.TextInput()
                                )

        length_of_substance = forms.ChoiceField(label='How long has the Person \
                                        had issues with substance abuse? ',
                                        choices = LOS_CHOICES,
                                        required = False,
                                        )

        length_of_substance_time = forms.CharField(label = 'Specify how long ',
                                required = False,
                                widget = forms.TextInput()
                                )

class KnowledgeAboutPersonInfo(forms.Form):
    pass

class IdentifyingInfo(forms.Form):
    race = forms.BooleanField(label = 'Race ', required = False,)
