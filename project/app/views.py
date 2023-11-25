from datetime import date,datetime
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
from app.forms import AuthenticateClient,RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView,View,TemplateView
from app.models import Client
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponse

#Mixin
class RequiredThreshold(object):
    def dispatch(self, request, *args, **kwargs):
        current_date = date.today()
        birth_date = request.user.birth_date

        if (current_date.year - birth_date.year) - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day)) < 18:
            return HttpResponse('Under 18, retry please')
        
        return super().dispatch(request, *args, **kwargs)
    

# Create your views here.
class LoginClient(LoginView):
    form_class = AuthenticateClient
    template_name = 'login.html'

class ChangePassword(LoginRequiredMixin,PasswordChangeView): 
    template_name = 'change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')
    login_url = reverse_lazy('login')

class RegisterClient(CreateView):
    model = Client
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class HomePage(LoginRequiredMixin,RequiredThreshold,TemplateView):
    template_name = 'home.html'
    login_url = reverse_lazy('login')

# reset password views
# по введенной почте найти в базе пользователя и сделать токен
def CheckEmail(request):
    if request.method == 'POST':
        sended_email = request.POST.get('email')
        user = Client.objects.get(email = sended_email)
        
        if user:
            token = default_token_generator.make_token(user)
            verify_url = request.build_absolute_uri(f'/reset/{user.pk}/{token}/')
            
            message = '''
            Привет {0}
            Нажмите на эту ссылку для того чтобы восстановить пароль от аккаунта : \n\n{1}
            '''.format(user.username,verify_url)

            send_mail('reset pass',message,'',[str(user.email)])
            return HttpResponse('проверьте свою почту')
        
    return render(request,'temp_reset.html')

def CheckTokenAndSaveChanges(request,user_pk,token):
    user = Client.objects.get(id=user_pk)
    if request.method == 'POST':
        if default_token_generator.check_token(user,token) == True:
            user.set_password(request.POST.get('password1'))
            user.save()
            
            return redirect('login')
    else:
        return render(request,'reset.html')