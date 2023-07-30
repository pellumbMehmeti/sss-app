from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.



def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in now!")
            return redirect('home')
        else: 
            messages.error(request, 'Sorry! There was an error logging in, Please Try Again...')
            return redirect('home')
    else: 
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out now")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})    