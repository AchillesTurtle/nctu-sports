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
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder' : 'Student ID', 'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder' : 'First Name', 'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder' : 'Last Name', 'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder' : 'Email', 'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder' : 'Password', 'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder' : 'Password Again', 'class' : 'form-control'})
        self.fields['captcha'].widget.attrs.update({'placeholder' : 'Enter the characters above', 'class' : 'form-control'})

        self.fields['username'].label='學號'
        self.fields['first_name'].label='名字'
        self.fields['last_name'].label='姓'
        self.fields['email'].label='電子郵件'
        self.fields['password1'].label='密碼'
        self.fields['password2'].label='確認密碼'
        self.fields['captcha'].label='輸入圖片中看到的英文及數字'