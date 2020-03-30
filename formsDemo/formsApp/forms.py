from django import forms
from django.core import validators
import re

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'),('female','FEMALE')]
    regex = '\d+'
    firstName = forms.CharField(validators=[validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    lastName = forms.CharField()
    email = forms.EmailField(validators=[validators.EmailValidator()])
    gender = forms.CharField(widget = forms.Select(choices=GENDER))
    password = forms.CharField(widget = forms.PasswordInput)
    ssn = forms.CharField(validators=[validators.RegexValidator(regex=regex),validators.MinLengthValidator(9),validators.MaxLengthValidator(9)])


"""
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        inputEmail = user_cleaned_data['email']
        print(inputFirstName, inputEmail)
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length of firstName is 20')
        elif inputEmail.find('@') == -1:
            print('check email get called')
            raise forms.ValidationError('The email should contains @')
        else:




    def clean_firstName(self):
        print('clean_firstName get called')
        inputFirstName = self.cleaned_data['firstName']
        print(inputFirstName)
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length of firstName is 20')
            return inputFirstName

    def clean_email(self):
        print('clean_email get called')
        inputEmail = self.cleaned_data['email']
        print(inputEmail)
        if inputEmail.find('@') == -1:
            raise forms.ValidationError('The email should contains @')
        return inputEmail
"""
