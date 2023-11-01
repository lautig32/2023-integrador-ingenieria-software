from django.views.generic import ListView
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension

class TeamListView(ListView):
    model = Team
    template_name = 'list/team_list.html'
    context_object_name = 'teams'

class MatchListView(ListView):
    model = Match
    template_name = 'list/match_list.html'
    context_object_name = 'matches'

class PlayerListView(ListView):
    model = Player
    template_name = 'list/player_list.html'
    context_object_name = 'players'