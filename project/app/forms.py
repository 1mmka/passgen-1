from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from app.models import Client

class AuthenticateClient(AuthenticationForm):
    class Meta:
        model = Client
        fields = ['username','password']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['username','password1','password2']