from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'finance/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('logged_in')
    else:
        form = AuthenticationForm()
    return render(request, 'finance/login.html', {'form': form})

def logged_in(request):
    return render(request, 'finance/logged_in.html')
