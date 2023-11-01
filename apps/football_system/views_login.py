from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import *

from .forms import *

def home(request):
    now = timezone.now()
    
    next_match = Match.objects.filter(date__gt=now).order_by('date').first()
    
    context = {
        'next_match': next_match,
    }
    
    return render(request, 'home.html', context)

def get_match_info(request, match_id):
    if request.method == "GET":
        try:
            # Consulta la base de datos para obtener la información del partido
            match = Match.objects.get(id=match_id)
            match_data = {
                'id': match.id,
                'date': match.date.strftime("%Y-%m-%dT%H:%M"),
                'local_team': match.local_team.name,
                'local_team_image': match.local_team_image.url,
                'visiting_team': match.visiting_team.name,
                'visiting_team_image': match.visiting_team_image.url,
                'local_team_result': 44,
                'visiting_team_result': 55
            }
            return JsonResponse(match_data)
        except Match.DoesNotExist:
            return JsonResponse({'error': 'Match not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        
        # Intentar autenticar con nombre de usuario
        user = authenticate(request, username=username_or_email, password=password)
        
        # Si no se encuentra con nombre de usuario, intentar autenticar con correo electrónico
        if user is None:
            try:
                user = Person.objects.get(email=username_or_email)
                user = authenticate(request, username=user.username, password=password)

            except Person.DoesNotExist:
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
        exists = Person.objects.filter(email=email).exists()
        return JsonResponse({'exists': exists})


@csrf_exempt
def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        exists = Person.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})


def signup(request):
    form = PersonForm()

    context = {
        'form': form,
    }
    
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
                'form': form,
            }

            return render(request, 'signup.html', context)
        
        if Person.objects.filter(username=username).exists():
            message = 'El nombre de usuario ya está en uso.'

            context = {
                'message': message,
                'email': email,
            }

            return render(request, 'signup.html', context) 
        
        if Person.objects.filter(email=email).exists():
            message = 'El correo electrónico ya está en uso.'

            context = {
                'message': message,
                'username': username,
            }

            return render(request, 'signup.html', context) 

        user = Person.objects.create_user(username=username, password=password, email=email)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        login(request, user)
        
        return redirect('home')  
    
    return render(request, 'signup.html', context=context)

def logout_view(request):

    logout(request)
    
    return render(request, 'home.html')

@login_required
def profile(request):
    user = request.user

    user_type_choices = Person.TypeAdministrator.choices

    clubs = Club.objects.all()

    try:
        person = Person.objects.get(pk=user.pk)
    except Person.DoesNotExist:
        person = None

    clubs = Club.objects.all()

    if person:    
        if request.method == 'POST':
            name = request.POST['user-name']
            email = request.POST['user-email']
            club = request.POST['user-club']
            user_type = request.POST['user-type']

            person = Person.objects.get(pk = user.pk)

            if name:
                person.first_name = name
            if email:
                person.email = email
            if club:
                person.club = Club.objects.get(pk=club)
            if user_type:
                person.type = user_type

            person.save_base()

        context = {
            'user': person,
            'clubs': clubs,
            'user_type_choices': user_type_choices,
        }

        return render(request, 'profile.html', context)
        
    else:
        return redirect('home')