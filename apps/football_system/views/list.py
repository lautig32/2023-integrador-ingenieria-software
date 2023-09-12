from django.views.generic import ListView
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension

class ClubListView(ListView):
    model = Club
    template_name = 'clubs.html'
    context_object_name = 'clubs'

class PersonListView(ListView):
    model = Person
    template_name = 'list/person_list.html'
    context_object_name = 'persons'

class FootballCategoryListView(ListView):
    model = FootballCategory
    template_name = 'list/football_category_list.html'
    context_object_name = 'football_categories'

class TeamListView(ListView):
    model = Team
    template_name = 'list/team_list.html'
    context_object_name = 'teams'

class MatchListView(ListView):
    model = Match
    template_name = 'matches.html'
    context_object_name = 'matches'

class PlayerListView(ListView):
    model = Player
    template_name = 'players.html'
    context_object_name = 'players'

class PlayerSuspensionListView(ListView):
    model = PlayerSuspension
    template_name = 'list/player_suspension_list.html'
    context_object_name = 'player_suspensions'
