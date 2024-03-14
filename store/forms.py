from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)

        self.fields['old_password'].label=""
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'current password'
        self.fields['old_password'].help_text= '<span class ="form-text text muted"><small>Please enter your current password</small></span>'


        self.fields['new_password1'].label=""
        self.fields['new_password1'].widget.attrs['class']="form-control"
        self.fields['new_password1'].widget.attrs['placeholder']="new password"
        self.fields['new_password1'].help_text= '<ul class = "form-text text-muted small"><li>Your Password can\'t be similar to your other personal information. </li><li>Your Password must contain at least 8 characters.</li><li>Your Password can\'t be commonly used password.</li><li>Your password can\'t be entirely numeric </li></ul>'

        self.fields['new_password2'].label=""
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'confirm new password'
        self.fields['new_password2'].help_text= '<span class ="form-text text muted"><small>Please confirm your new password</small></span>'


class UpdateUserProfile(UserChangeForm):
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'FirstName'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'LastName', }))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserProfile, self).__init__(*args, **kwargs)


        self.fields['username'].label =""
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['placeholder']='username'
        self.fields['username'].help_text= '<span class = "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digit and @/./+/-/_only000.</small></span>'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

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