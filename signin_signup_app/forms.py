from django import forms

from .models import User

class UserSignupForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "E-Mail"}))
    # password = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password"}))
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password'
        ]
        widgets = {
            'name'     : forms.TextInput(attrs={"placeholder": "Username"}),
            'email'    : forms.TextInput(attrs={"placeholder": "E-Mail"}),
            'password' : forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
    
class UserSigninForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    # password = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password"}))
    class Meta:
        model = User
        fields = [
            'name',
            'password'
        ]
        widgets = {
            'name'     : forms.TextInput(attrs={"placeholder": "Username"}),
            'password' : forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }