import string

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    signature = forms.CharField(widget=forms.HiddenInput, max_length=132)

    def __init__(self, token, *args, **kwargs):
        self.token = token
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_signature(self):
        sig = self.cleaned_data['signature']

        if len(sig) != 132 or (sig[130:] != '1b' and  sig[130:] != '1c') or not all(c in string.hexdigits for c in sig[2:]):
            raise forms.ValidationError('Invalid signature')

        self.user = authenticate(token=self.token, signature=sig)
        return sig


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
