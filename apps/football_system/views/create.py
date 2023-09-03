from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ..models import Club, Person, FootballCategory, Team, Match, Player, PlayerSuspension
from ..forms import ClubForm, PersonForm, FootballCategoryForm, TeamForm, MatchForm, PlayerForm, PlayerSuspensionForm

class ClubCreateView(CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'create/club_form.html'
    success_url = reverse_lazy('club_list')

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'create/person_form.html'
    success_url = reverse_lazy('person_list')

class FootballCategoryCreateView(CreateView):
    model = FootballCategory
    form_class = FootballCategoryForm
    template_name = 'create/football_category_form.html'
    success_url = reverse_lazy('football_category_list')

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'create/team_form.html'
    success_url = reverse_lazy('team_list')

class MatchCreateView(CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'create/match_form.html'
    success_url = reverse_lazy('match_list')

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'create/player_form.html'
    success_url = reverse_lazy('player_list')

class PlayerSuspensionCreateView(CreateView):
    model = PlayerSuspension
    form_class = PlayerSuspensionForm
    template_name = 'create/player_suspension_form.html'
    success_url = reverse_lazy('player_suspension_list')
