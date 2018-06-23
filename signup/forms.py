from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder' : 'Student ID'})
        self.fields['first_name'].widget.attrs.update({'placeholder' : 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder' : 'Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder' : 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder' : 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder' : 'Password Again'})
        self.fields['captcha'].widget.attrs.update({'placeholder' : 'Enter the characters above'})