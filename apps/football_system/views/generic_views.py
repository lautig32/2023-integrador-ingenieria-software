from django.shortcuts import render, redirect
from . .models import *

def views_matches(request):
    user = request.user

    try:
        person = Person.objects.get(pk=user.pk)
    except Person.DoesNotExist:
        person = None

    if person:
        if person.type == Person.TypeAdministrator.PLANNER:
            if request.method == 'POST':
                if 'form-match-create' in request.POST:
                    category = request.POST['category']
                    local_team = request.POST['local_team']
                    visiting_team = request.POST['local_team']

                    if category and local_team and visiting_team:
                        Match.objects.get_or_create(
                            category=category, 
                            local_team=local_team, 
                            visit_team=visiting_team
                        )

                elif 'form-match-edit' in request.POST:
                    pk = request.POST['id']
                    category = request.POST['category']
                    local_team = request.POST['local_team']
                    visiting_team = request.POST['local_team']

                    match = Match.objects.get(pk=pk)

                    match.category = category
                    match.local_team = local_team
                    match.visiting_team = visiting_team
                    match.save_base()

            context = {
                'user': person,
                'matches': Match.objects.all(),
            }

            return render(request, 'matches.html', context)

        else:
            context = {
                'user': person,
                'matches': Match.objects.all(),
            }
            
            return render(request, 'matches.html', context)
    else:
        context = {
            'matches': Match.objects.all(),
        }

        return render(request, 'matches.html', context)

def views_clubs(request):
    user = request.user

    try:
        person = Person.objects.get(pk=user.pk)
    except Person.DoesNotExist:
        person = None

    if person:
        if person.type == Person.TypeAdministrator.TECHNICAL_DIRECTOR:

            if request.method == 'POST':
                if 'form-player-create' in request.POST:
                    name = request.POST['name']
                    team = request.POST['team']

                    if name and team:
                        Player.objects.get_or_create(name=name, team=team)

                elif 'form-player-edit' in request.POST:
                    pk = request.POST['id']
                    name = request.POST['name']
                    team = request.POST['team']

                    player = Player.objects.get(pk=pk)

                    player.name = name
                    player.team = team
                    player.save_base()

                elif 'form-team-create' in request.POST:
                    name = request.POST['name']
                    club = request.POST['club']
                    category = request.POST['category']  

                    if name and club and category:
                        Team.objects.get_or_create(name=name, club=club, category=category)

                elif 'form-team-edit' in request.POST:
                    pk = request.POST['id']
                    name = request.POST['name']
                    club = request.POST['club']
                    category = request.POST['category']            

                    team = Team.objects.get(pk=pk)

                    team.name = name
                    team.club = Club.objects.get(pk=club)
                    team.category = FootballCategory.objects.get(pk=category)
                    team.save_base()

            context = {
                'user': person,
                'clubs': Club.objects.get(pk=person.club.pk),
                'teams': Team.objects.filter(club=person.club),
                'players': Player.objects.filter(team__club=person.club),
            }

            return render(request, 'clubs.html', context)
        
        else:
            return redirect('home')
        
    else:
        return redirect('home')
