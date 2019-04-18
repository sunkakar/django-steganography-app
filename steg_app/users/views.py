from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            UserName = form.cleaned_data.get('username')
            messages.success(request, f'{UserName}: Account Created!')
            return redirect('welcome-page')
    else:
        form = UserCreationForm()
    return render(request,'users/signup.html', {'form': form})