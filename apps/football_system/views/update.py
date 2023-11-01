from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension
from ..forms import TeamForm, MatchForm, PlayerForm

class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'update/team_update.html'
    success_url = reverse_lazy('team_list')

class MatchUpdateView(UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'update/match_update.html'
    success_url = reverse_lazy('match_list')

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'update/player_update.html'
    success_url = reverse_lazy('player_list')