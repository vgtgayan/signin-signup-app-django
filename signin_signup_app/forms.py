from django import forms

from .models import User

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password'
        ]
        widgets = {
            'password' : forms.PasswordInput(),
        }
    
class UserSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'password'
        ]
        widgets = {
            'password' : forms.PasswordInput(),
        }