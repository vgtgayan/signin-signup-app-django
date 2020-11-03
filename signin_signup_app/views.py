from django.shortcuts import render
from .forms import (
                UserSignupForm,
                UserSigninForm
)

# How to use 2 forms in one html template? How will they handle POST request?
def signin_view(request):
    signup_form = UserSignupForm(request.POST or None)
    if signup_form.is_valid():
        signup_form.save()
        signup_form = UserSignupForm()
    
    
    context = {
        'signup_form' : signup_form
    }

    return render(request, 'signin_signup_app/index.html', context)