from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
def account_view(request):
    return render(request, 'accounts/account.html')

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(username=data['user_name'] , first_name=data['first_name'] , last_name=data['last_name'] , email=data['email'] , password=data['password_1'])
            return redirect('home:home')
    else:
        form = UserRegisterForm(request.GET)
        return render(request,'accounts/account.html',{'form': form}) 
    

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data['user'], password = data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home') 
            
    else:
        form = UserLoginForm() 
    return render(request , 'accounts/login.html', {'form' : form}) 
