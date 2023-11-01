from django import forms

from .models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'club', 'category', 'logo']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['category', 'date', 'local_team', 'local_team_image', 'local_team_goals', 'visiting_team', 'visiting_team_image', 'visiting_team_goals']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

class CreateMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['category', 'date', 'local_team', 'local_team_image', 'visiting_team', 'visiting_team_image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'datetime-local'}),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name','surname', 'team', 'photo']

