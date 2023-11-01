from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension
from ..forms import TeamForm, MatchForm, PlayerForm

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'create/team_create.html'
    success_url = reverse_lazy('team_list')

class MatchCreateView(CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'create/match_create.html'
    success_url = reverse_lazy('match_list')

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'create/player_create.html'
    success_url = reverse_lazy('player_list')
