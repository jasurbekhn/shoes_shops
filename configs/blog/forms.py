from django import forms
from .models import Article
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'content',
                  'photo',
                  'category',
                  'video')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nomlanishi'
            }),
            'content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Tarifi'
            }),
            'photo': forms.FileInput(attrs={
                'class': "form-control"
            }),
            'category': forms.Select(attrs={
                'class': "form-control"
            }),
            'video': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Video uchun havola'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, help_text="Maksimum 16 belgi va harf kiriting!",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Login'
                               }))

    password = forms.CharField(label='Parol',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Parol'
                               }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol tasdiqlash'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Taxallus ism'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ism'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Familiya'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  )
