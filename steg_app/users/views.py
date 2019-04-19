from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Print message
            UserName = form.cleaned_data.get('username')
            messages.success(request, f'{UserName}: Account Created!')
            return redirect('login')
        #else:
    else:
        form = UserSignUpForm()
    return render(request,'users/signup.html', {'form': form})