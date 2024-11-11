from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введіть email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть email'})
    )
    username = forms.CharField(
        label="Введіть ім'я користувача",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введіть ім'я користувача"
        })
    )
    password1 = forms.CharField(
        label='Введіть пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password2 = forms.CharField(
        label='Введіть підтвердження паролю',
        required=True,
        help_text='Паролі мають збігатись',
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']