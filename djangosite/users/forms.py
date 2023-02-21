from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Логін'}))

    email = forms.EmailField(label='Пошта',
                             widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Пошта'}))

    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'input_text', 'placeholder': 'Пароль'}))

    password2 = forms.CharField(label='Пароль2',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'input_text', 'placeholder': 'Повтор паролю'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input_text', 'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'input_text', 'placeholder': "Прізвище"}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Логін'}))

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'input_text', 'placeholder': 'Пароль'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Пошта',
                             widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'Пошта'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input_text', 'placeholder': "Ім'я"}),
            'last_name': forms.TextInput(attrs={'class': 'input_text', 'placeholder': "Прізвище"}),
        }


class UserProfileUpdateForm(forms.ModelForm):
    image = forms.FileField(label='Фото',
                            widget=forms.FileInput(attrs={'class': 'input_file', 'accept': '.jpg, .png, .jpeg'}))

    class Meta:
        model = UserProfile
        fields = ['image']


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'input_text',
        'placeholder': 'Пошта',
        'type': 'email',
        'name': 'email'
    }))
