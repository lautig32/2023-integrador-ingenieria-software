from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension
from ..forms import TeamForm, MatchForm, PlayerForm

class ClubDeleteView(DeleteView):
    model = Club
    template_name = 'delete/club_confirm_delete.html'
    success_url = reverse_lazy('club_list')

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'delete/person_confirm_delete.html'
    success_url = reverse_lazy('person_list')

class FootballCategoryDeleteView(DeleteView):
    model = FootballCategory
    template_name = 'delete/football_category_confirm_delete.html'
    success_url = reverse_lazy('football_category_list')

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'delete/team_confirm_delete.html'
    success_url = reverse_lazy('team_list')

class MatchDeleteView(DeleteView):
    model = Match
    template_name = 'delete/match_confirm_delete.html'
    success_url = reverse_lazy('match_list')

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'delete/player_confirm_delete.html'
    success_url = reverse_lazy('player_list')

class PlayerSuspensionDeleteView(DeleteView):
    model = PlayerSuspension
    template_name = 'delete/player_suspension_confirm_delete.html'
    success_url = reverse_lazy('player_suspension_list')
