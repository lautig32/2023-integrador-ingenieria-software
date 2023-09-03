from django import forms

from .models import *

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'email', 'password', 'type', 'profile_picture', 'club']


class FootballCategoryForm(forms.ModelForm):
    class Meta:
        model = FootballCategory
        fields = ['name']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'club', 'category', 'logo']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['category', 'local_team', 'visiting_team', 'local_team_image', 'visiting_team_image', 'date']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team', 'photo']


class PlayerSuspensionForm(forms.ModelForm):
    class Meta:
        model = PlayerSuspension
        fields = ['player', 'start_date', 'num_matches', 'reason']