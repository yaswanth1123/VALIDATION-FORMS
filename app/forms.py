from django import forms
import django
from django.core import validators

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name starts with a')


def check_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('len is greater than 5')


class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    email=forms.EmailField()
    remail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])


def clean(self):
    e=self.cleaned_data.get('email')
    r=self.cleaned_data.get('remail')
    if e!=r:
        raise forms.ValidationError('emails not matched')

def clean_botchtcher(self):
    bot=self.cleaned_data.get('botcatcher')
    if len(bot)>0:
        raise forms.ValidationError('bot has catched')