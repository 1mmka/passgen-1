from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from app.models import Client
from django import forms

class AuthenticateClient(AuthenticationForm):
    class Meta:
        model = Client
        fields = ['username','password']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['username','password1','password2','email','birth_date']
        widgets = {
            'birth_date' : forms.DateInput(attrs={'type':'date'})
        }