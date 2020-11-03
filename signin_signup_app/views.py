from django.shortcuts import render
from .forms import UserForm

# How to use 2 forms in one html template? How will they handle POST request?
def signin_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    form = UserForm()
    
    context = {
        'form' : form
    }

    return render(request, 'signin_signup_app/index.html', context)