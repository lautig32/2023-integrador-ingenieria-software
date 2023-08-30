from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def home(request):
    
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        
        # Intentar autenticar con nombre de usuario
        user = authenticate(request, username=username_or_email, password=password)
        
        # Si no se encuentra con nombre de usuario, intentar autenticar con correo electrónico
        if user is None:
            try:
                user = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user.username, password=password)
            except User.DoesNotExist:
                pass
        
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


@csrf_exempt
def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        exists = User.objects.filter(email=email).exists()
        return JsonResponse({'exists': exists})

@csrf_exempt
def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            message = 'Las contraseñas no coinciden.'

            context = {
                'message': message,
                'email': email,
                'username': username,
            }

            return render(request, 'signup.html', context)
        
        if User.objects.filter(username=username).exists():
            message = 'El nombre de usuario ya está en uso.'

            context = {
                'message': message,
                'email': email,
            }

            return render(request, 'signup.html', context) 
        
        if User.objects.filter(email=email).exists():
            message = 'El correo electrónico ya está en uso.'

            context = {
                'message': message,
                'username': username,
            }

            return render(request, 'signup.html', context) 

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

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass
    
    return render(request, 'matches.html')

def teams(request):
    
    return render(request, 'teams.html')