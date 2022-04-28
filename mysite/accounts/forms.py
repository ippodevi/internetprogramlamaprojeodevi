from django import forms
from django.contrib.auth.forms import UserCreationForm #django içindeki formu kullanmak için
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı adı'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Şifre'
    }))
    
class RegisterForm(UserCreationForm): #var olan UserCreation Form u extend ettik.
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'İsim'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyisim'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı Adı'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-mail'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Şifre'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Şifrenizi tekrar giriniz'
    }))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']