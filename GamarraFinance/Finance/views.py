from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm


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
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('logged_in')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'finance/login.html', {'form': form})

def logged_in(request):
    return render(request, 'finance/logged_in.html')
