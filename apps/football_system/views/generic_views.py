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
                    category = request.POST['match-category']
                    local_team = request.POST['match-local-team']
                    visiting_team = request.POST['match-visiting-team']
                    date = request.POST['match-date']

                    if category and local_team and visiting_team:
                        Match.objects.create(
                            category=FootballCategory.objects.get(pk=category), 
                            local_team=Team.objects.get(pk=local_team), 
                            visiting_team=Team.objects.get(pk=visiting_team),
                            date = date,
                        )

                elif 'form-match-edit' in request.POST:
                    pk = request.POST['id']
                    category = request.POST['match-category']
                    local_team = request.POST['match-local-team']
                    visiting_team = request.POST['match-visiting-team']

                    match = Match.objects.get(pk=pk)

                    match.category = category
                    match.local_team = local_team
                    match.visiting_team = visiting_team
                    match.save_base()

            context = {
                'user': person,
                'matches': Match.objects.all(),
                'teams': Team.objects.all(),
                'categories': FootballCategory.objects.all(),
            }

            return render(request, 'matches.html', context)

        else:
            context = {
                'user': person,
                'matches': Match.objects.all(),
                'categories': FootballCategory.objects.all(),
            }
            
            return render(request, 'matches.html', context)
    else:
        context = {
            'matches': Match.objects.all(),
            'categories': FootballCategory.objects.all(),
        }

        return render(request, 'matches.html', context)

def views_clubs(request):
    user = request.user

    try:
        person = Person.objects.get(pk=user.pk)
    except Person.DoesNotExist:
        person = None

    print(person)

    if person:
        if person.type == Person.TypeAdministrator.TECHNICAL_DIRECTOR:
            print("User valid")
            if request.method == 'POST':
                print("request post")
                if 'form-player-create' in request.POST:
                    name = request.POST['player-name']
                    team = request.POST['player-team']
                    print(name, team)
                    if name and team:
                        team = Team.objects.get(pk=team)
                        Player.objects.get_or_create(name=name, team=team)

                elif 'form-player-edit' in request.POST:
                    pk = request.POST['id']
                    name = request.POST['player-name']
                    team = request.POST['player-team']

                    player = Player.objects.get(pk=pk)

                    player.name = name
                    player.team = Team.objects.get(pk=team)
                    player.save_base()

                elif 'form-team-create' in request.POST:
                    name = request.POST['team-name']
                    category = request.POST['team-category']  

                    if name and category:
                        category = FootballCategory.objects.get(pk=category)
                        club = person.club
                        Team.objects.get_or_create(name=name, club=club, category=category) 

                elif 'form-team-edit' in request.POST:
                    pk = request.POST['id']
                    name = request.POST['team-name']
                    club = request.POST['team-club']
                    category = request.POST['team-category']

                    team.name = name
                    team.club = Club.objects.get(pk=club)
                    team.category = FootballCategory.objects.get(pk=category)
                    team.save_base()

            context = {
                'user': person,
                'clubs': Club.objects.filter(pk=person.club),
                'teams': Team.objects.filter(club=person.club),
                'players': Player.objects.filter(team__club=person.club),
                'categories': FootballCategory.objects.all(),
            }
            print(context)
            return render(request, 'clubs.html', context)
        
        else:
            return redirect('home')
        
    else:
        return redirect('home')
