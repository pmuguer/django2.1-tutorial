from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


def validate_gcba_email(email):
    if not email.split("@")[1].startswith("buenosaires"):
        raise ValidationError('El mail no pertenece al gcba',
                              code='invalid_email', params={'value': email})


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(validators=[validate_gcba_email])
    #sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
