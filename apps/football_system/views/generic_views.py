from django.shortcuts import render, redirect
from . .models import Match, Club, Person

def views_matches(request):
    user = request.user

    try:
        person = Person.objects.get(pk=user.pk)
    except Person.DoesNotExist:
        person = None

    matches = Match.objects.all()

    if person:
        context = {
            'user': person,
            'matches': matches,
        }

        if person.type == Person.TypeAdministrator.PLANNER or person.type == Person.TypeAdministrator.TECHNICAL_DIRECTOR:

            if request.method == 'POST':
                pass

            return render(request, 'matches.html', context)
        
        else:
            return render(request, 'matches.html', context)
    else:
        context = {
            'matches': matches,
        }

        return render(request, 'matches.html', context)

def views_clubs(request):
    user = request.user

    try:
        person = Person.objects.get(pk=user.pk)
    except Person.DoesNotExist:
        person = None

    clubs = Club.objects.all()

    if person:
        context = {
            'user': person,
            'clubs': clubs,
        }

        if person.type == Person.TypeAdministrator.PLANNER or person.type == Person.TypeAdministrator.TECHNICAL_DIRECTOR:

            if request.method == 'POST':
                pass

            return render(request, 'clubs.html', context)
        
        else:
            return redirect('home')
        
    else:
        return redirect('home')
