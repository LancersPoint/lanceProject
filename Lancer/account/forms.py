from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField
from django_countries import widgets, countries
from django_countries.widgets import CountrySelectWidget


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput)
     

class UserRegistratioinForm(forms.ModelForm):
    photo = forms.ImageField(required=True)
    resume = forms.FileField(required=True)
    title = forms.CharField()
    date_of_birth = forms.DateField(required=True)
    username = forms.CharField(max_length=20, min_length=8)
    country = forms.ChoiceField(widget=CountrySelectWidget, choices=countries)
    phone_number = PhoneNumberField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ( 'first_name','last_name', 'username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

# enable users edit thier profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('resume','date_of_birth', 'photo', 'phone_number', 'send_mail')
