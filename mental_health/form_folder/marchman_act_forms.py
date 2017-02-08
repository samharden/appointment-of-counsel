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
    question_9 = forms.BooleanField(label = '', required = False,)
    question_9_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why (i.e., observation, related knowledge, etc.).',
                            })
                            )
    question_10 = forms.BooleanField(label = '', required = False,)
    question_10_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why (i.e., observation, related knowledge, etc.).',
                            })
                            )
    question_11 = forms.BooleanField(label = '', required = False,)
    question_11_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why (i.e., observation, related knowledge, etc.).',
                            })
                            )
    question_12 = forms.BooleanField(label = '', required = False,)
    question_12_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why (i.e., observation, related knowledge, etc.).',
                            })
                            )

    question_13 = forms.BooleanField(label = '', required = False,)

    question_13_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why (i.e., observation, related knowledge, etc.).',
                            })
                            )
    question_14 = forms.BooleanField(label = '', required = False,)
    question_14_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why (i.e., observation, related knowledge, etc.).',
                            })
                            )

    question_15a = forms.BooleanField(label = '', required = False,)
    question_15a_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain how.',
                            })
                            )

    question_15b = forms.BooleanField(label = '', required = False,)
    question_15b_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why.',
                            })
                            )

    question_15c = forms.BooleanField(label = '', required = False,)
    question_15c_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If checked, explain why.',
                            })
                            )


class IdentifyingInfo(forms.Form):

        respondent_county = forms.CharField(label = 'County of residence ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )
        respondent_age = forms.CharField(label = 'Age ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )
        respondent_race = forms.CharField(label = 'Race',
                                    required = False,
                                    widget = forms.TextInput()
                                    )
        respondent_sex = forms.ChoiceField(label = 'Sex ',
                                    choices = SEX_CHOICES,
                                    required = False,
                                    )
        respondent_ssn = forms.CharField(label = 'SSN ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )
        respondent_height = forms.CharField(label = 'Height ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )

        respondent_weight = forms.CharField(label = 'Weight ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )



        respondent_haircolor = forms.CharField(label = 'Hair color ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )


        respondent_eyecolor = forms.CharField(label = 'Eye color ',
                                    required = False,
                                    widget = forms.TextInput()
                                    )


class ViolenceInfo(forms.Form):
    question_16 = forms.ChoiceField(label = 'Does the person have access to any \
                                            weapons?', required = False,
                                            choices = YNM_CHOICES,)
    question_16_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If you believe the person has access to any weapons, please describe.',
                            })
                            )

    question_17 = forms.ChoiceField(label = 'Is the person violent now?',
                                    required = False,
                                    choices = YNM_CHOICES,)
    question_17_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If you believe the person is violent now, please describe.',
                            })
                            )

    question_18 = forms.ChoiceField(label = 'Has the person been violent toward anyone, including law enforcement, in the recent past?',
                                            required = False,
                                            choices = YNM_CHOICES,)
    question_18_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If the person has been violent toward anyone, please describe.',
                            })
                            )

    question_19 = forms.ChoiceField(label = 'Does the person have any pending \
                                            criminal charges against them?',
                                            required = False,
                                            choices = YNM_CHOICES,)
    question_19_desc = forms.CharField(label = '',
                            required = False,
                            widget = forms.Textarea(attrs={
                            'placeholder': 'If the person has pending criminal charges, please describe. Example: they have a DUI case in Pinellas county.',
                            })
                            )



class AttyGuardianInfo(forms.Form):
    question_20 = forms.ChoiceField(label = 'Does the person have an attorney?',
                                            required = False,
                                            choices = YNM_CHOICES,)
    question_20_desc = forms.CharField(label = "If they do, please provide the attorney's name:",
                            required = False,
                            widget = forms.TextInput(attrs={
                            'placeholder': 'Attorney Name',
                            })
                            )

    question_21 = forms.ChoiceField(label = 'Can the person afford an attorney?',
                                            required = False,
                                            choices = YN_CHOICES,)

    question_22 = forms.ChoiceField(label = 'Does the person have a legal guardian?',
                                            required = False,
                                            choices = YNM_CHOICES,)

    question_23 = forms.ChoiceField(label = "Is there a pending petition to determine \
                                            the Person's capacity and to appoint a guardian?",
                                            required = False,
                                            choices = YNM_CHOICES,)

    guardian_name = forms.CharField(label = "Guardian's name",
                            required = False,
                            widget = forms.TextInput(attrs={
                            'placeholder': 'Name',
                            })
                            )
    guardian_phone = forms.CharField(label = "Guardian's phone",
                            required = False,
                            widget = forms.TextInput(attrs={
                            'placeholder': 'Phone',
                            })
                            )
    guardian_address = forms.CharField(label = 'Address',
                                required = True,
                                widget = forms.TextInput()
                                )

    guardian_city = forms.CharField(label = 'City ',
                                required = True,
                                widget = forms.TextInput()
                                )

    guardian_state = forms.ChoiceField(label = 'State ',
                                choices = STATE_CHOICES,
                                required = False,
                                )

    guardian_zip = forms.CharField(label = 'Zip ',
                                required = True,
                                widget = forms.TextInput()
                                )

    physician_name = forms.CharField(label = "Physician’s name",
                            required = False,
                            widget = forms.TextInput(attrs={
                            'placeholder': 'Name',
                            })
                            )
    physician_phone = forms.CharField(label = "Physician’s phone",
                            required = False,
                            widget = forms.TextInput(attrs={
                            'placeholder': 'Phone',
                            })
                            )


class PictureID(forms.Form):
        image = forms.ImageField(label = 'If you have a current picture of the person, you can attach it here: ',
                                    required = False,)























































###############################################################################
