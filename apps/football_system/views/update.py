from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension
from ..forms import ClubForm, PersonForm, FootballCategoryForm, TeamForm, MatchForm, PlayerForm, PlayerSuspensionForm

class ClubUpdateView(UpdateView):
    model = Club
    form_class = ClubForm
    template_name = 'update/club_form.html'
    success_url = reverse_lazy('club_list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'update/person_form.html'
    success_url = reverse_lazy('person_list')

class FootballCategoryUpdateView(UpdateView):
    model = FootballCategory
    form_class = FootballCategoryForm
    template_name = 'update/football_category_form.html'
    success_url = reverse_lazy('football_category_list')

class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'update/team_form.html'
    success_url = reverse_lazy('team_list')

class MatchUpdateView(UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'update/match_form.html'
    success_url = reverse_lazy('match_list')

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'update/player_form.html'
    success_url = reverse_lazy('player_list')

class PlayerSuspensionUpdateView(UpdateView):
    model = PlayerSuspension
    form_class = PlayerSuspensionForm
    template_name = 'update/player_suspension_form.html'
    success_url = reverse_lazy('player_suspension_list')
