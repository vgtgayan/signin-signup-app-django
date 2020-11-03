from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
                UserSignupForm,
                UserSigninForm
)
from .models import User


def signin_view(request):
    signup_form = UserSignupForm(request.POST or None)
    if signup_form.is_valid():
        try:
            user = User.objects.get(name=signup_form.cleaned_data['name'])
            return HttpResponse("<h1>Username already exists!.</h1>")
        except User.DoesNotExist:
            signup_form.save()
            signup_form = UserSignupForm()
    
    signin_form = UserSigninForm(request.POST or None)
    if signin_form.is_valid():
        try:
            user = User.objects.get(name=signin_form.cleaned_data['name'])
        except User.DoesNotExist:
            return redirect('/')
        if user.password == signin_form.cleaned_data['password']:
            return HttpResponse("<h1>You have logged in</h1>")

    
    context = {
        'signup_form' : signup_form,
        'signin_form' : signin_form
    }

    return render(request, 'signin_signup_app/index.html', context)