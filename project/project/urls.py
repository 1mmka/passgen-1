from django.contrib import admin
from django.urls import path
from app.views import LoginClient,home,ChangePassword,RegisterClient,CheckEmail,CheckTokenAndSaveChanges

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginClient.as_view(),name='login'),
    path('home',home,name='home'),
    path('change',ChangePassword.as_view(),name='change'),
    path('register',RegisterClient.as_view(),name='register'),
    path('check-email',CheckEmail,name='check_email'),
    path('reset/<int:user_pk>/<str:token>/',CheckTokenAndSaveChanges,name='check_token_and_reset'),
]