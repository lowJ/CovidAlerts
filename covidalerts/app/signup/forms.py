from django import forms
from signup.fields import ListTextWidget

class SignupForm(forms.Form):
    char_field_with_list = forms.CharField(required=True)
    def __init__(self, *args, **kwargs):
        _country_list = kwargs.pop('data_list', None)
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_country_list, name='country-list')