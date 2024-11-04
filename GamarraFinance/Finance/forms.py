from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password', 
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'address', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("E-mail already in use")
        return email

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
