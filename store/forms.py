from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstName = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    lastName = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))


    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


        self.fields['username'].label =""
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['username'].help_text= '<span class = "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digit and @/./+/-/_only000.</small></span>'


        self.fields['password1'].label=""
        self.fields['password1'].widget.attrs['class']="form-control"
        self.fields['password1'].widget.attrs['placeholder']="password"
        self.fields['password1'].help_text= '<ul class = "form-text text-muted small"><li>Your Password can\'t be similar to your other personal information. </li><li>Your Password must contain at least 8 characters.</li><li>Your Password can\'t be commonly used password.</li><li>Your password can\'t be entirely numeric </li></ul>'

        self.fields['password2'].label=""
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['password2'].help_text= '<span class ="form-text text muted"><small>Please confirm your password</small></span>'