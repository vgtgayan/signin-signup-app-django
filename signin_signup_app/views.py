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
            return render(request, 'signin_signup_app/signup_page.html', {})
    
    valid_pwd = True
    valid_usr = True
    signin_form = UserSigninForm(request.POST or None)    
    # Used ('email' not in request.POST) to distinguish from signup form request.POST
    if signin_form.is_valid() and ('email' not in request.POST):
        try:
            user = User.objects.get(name=signin_form.cleaned_data['name'])
            if user.password == signin_form.cleaned_data['password']:
                # return HttpResponse("<h1>You have logged in</h1>")
                return render(request, 'signin_signup_app/signin_page.html', {})
            else:
                # return HttpResponse("<h1>Incorrect Password</h1>")
                valid_pwd = False
        except User.DoesNotExist:
            valid_usr = False
            # return redirect('/')
        

    
    context = {
        'signup_form' : signup_form,
        'signin_form' : signin_form,
        'valid_pwd'   : valid_pwd,
        'valid_usr'   : valid_usr
    }

    return render(request, 'signin_signup_app/index.html', context)