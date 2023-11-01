import os
import io
from django.shortcuts import render, redirect
from . .models import *

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
                    logo = request.FILES.get('team-logo', None)  # Accede al campo de archivo usando request.FILES

                    if name and category and logo:
                        # Abre el archivo en modo lectura
                        with open(logo.name, 'rb') as logo_file:
                            # Lee el contenido del archivo y almacénalo en un búfer
                            buffer = io.BytesIO(logo_file.read())

                        # Realiza operaciones con el contenido del búfer, como guardar en el campo 'logo' del modelo Team
                        category = FootballCategory.objects.get(pk=category)
                        club = person.club
                        team, created = Team.objects.get_or_create(name=name, club=club, category=category)

                        # Guarda el contenido del búfer en el campo 'logo' del objeto Team
                        team.logo.save(str(logo), buffer, save=True)

                        buffer.close()

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
                'clubs': Club.objects.filter(pk=person.club.pk),
                'teams': Team.objects.filter(club=person.club),
                'players': Player.objects.filter(team__club=person.club),
                'categories': FootballCategory.objects.all(),
            }

            return render(request, 'clubs.html', context)
        
        else:
            return redirect('home')
        
    else:
        return redirect('home')
