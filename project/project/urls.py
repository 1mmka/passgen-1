from django.contrib import admin
from django.urls import path
from app.views import LoginClient,home,ChangePassword,RegisterClient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginClient.as_view(),name='login'),
    path('home',home,name='home'),
    path('change',ChangePassword.as_view(),name='change'),
    path('register',RegisterClient.as_view(),name='register')
]
