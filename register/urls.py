from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('reg/', views.register, name='reg'),
    path('user/',auth.LoginView.as_view(template_name='register/user.html'), name='user'),
    path('exit/',auth.LogoutView.as_view(template_name='register/exit.html'), name='exit')
]