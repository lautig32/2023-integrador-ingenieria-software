from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('signup') 
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('signup')  

        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
     
        login(request, user)
        
        return redirect('home')  
    
    return render(request, 'signup.html')

def logout_view(request):

    logout(request)
    
    return render(request, 'home.html')

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