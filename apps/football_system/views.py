from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            message = 'Nombre de usuario o contraseña incorrectos.'

            context = {
                'message': message
            }

            return render(request, 'login.html', context)

    return render(request, 'login.html')

def signup(request):
    
    return render(request, 'signup.html')

def profile(request):
    user = request.user

    context = {
        'user': user
    }

    return render(request, 'profile.html', context)

def matches(request):
    
    return render(request, 'matches.html')

def teams(request):
    
    return render(request, 'teams.html')