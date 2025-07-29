from django import forms
from django.contrib.auth.models import User
class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    password_1 = forms.CharField(max_length=100)
    password_2 = forms.CharField(max_length=100)


    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username = user).exists():
            raise forms.ValidationError('uesr exists')
        return user
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('email exist')
        return email
    

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1'] 
        password_2 = self.cleaned_data['password_2']
        if password_1 != password_2:
            raise forms.ValidationError("password is unmatch")
        elif len(password_2) <8 :
            raise ValueError("password is short")
        elif not any(x.isupper for x in password_2):
            raise forms.ValidationError("use upper char")
        return password_2 
    

class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)