from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                
                else:
                    messages.info(request, 'Kullanıcı aktif değil')
                    
            else:
                messages.info(request, 'Şifre veya kullanıcı adınızı yanlış girdiniz.')
                
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form':form})

def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()                                                                                                                                                                                                                                                                 
            messages.success(request, 'Hesap oluşturuldu.') #request aldıgı zaman mesajımızı olusturduk.
            return redirect('login') 
    
    else:
        form = RegisterForm()
    
    
    return render(request,'register.html',{'form':form})

def user_logout(request):
    pass

def user_dashboard(request):
    pass

def index(request):
    return render(request, 'index.html')
# Create your views here.
