from django.shortcuts import render

def home(request):
    
    return render(request, 'home.html')

def login(request):
    
    return render(request, 'login.html')

def signup(request):
    
    return render(request, 'signup.html')

def profile(request):
    
    return render(request, 'profile.html')

def matches(request):
    
    return render(request, 'matches.html')

def teams(request):
    
    return render(request, 'teams.html')