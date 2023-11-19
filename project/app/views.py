from django.shortcuts import render
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
from app.forms import AuthenticateClient,RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView
from app.models import Client

# Create your views here.
class LoginClient(LoginView):
    form_class = AuthenticateClient
    template_name = 'login.html'

class ChangePassword(LoginRequiredMixin,PasswordChangeView): # для получения доступа к этим представлениям пользователь должен быть авторизованным
    template_name = 'change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

class RegisterClient(CreateView):
    model = Client
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

def home(request):
    return render(request,'home.html')