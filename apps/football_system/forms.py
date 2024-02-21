from django import forms

from .models import *

from django import forms
from django.utils.safestring import mark_safe

from .models import *

class CreatePlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'surname', 'team']


class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'club', 'category']


class CreateMatchForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Match
        fields = ['category', 'date', 'local_team', 'visiting_team']


class LogoWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, 'url'):
            output.append(f'<a href="{value.url}" target="_blank"><img src="{value.url}" alt="{name} Logo" style="max-width: 200px;" /></a><br>')
        output.append(super().render(name, value, attrs, renderer))
        return mark_safe(''.join(output))

class PlayerForm(forms.ModelForm):
    photo = forms.ImageField(widget=LogoWidget)
    class Meta:
        model = Player
        fields = ['name', 'surname', 'team', 'is_suspended','photo']


class TeamForm(forms.ModelForm):
    logo = forms.ImageField(widget=LogoWidget)
    class Meta:
        model = Team
        fields = ['name', 'club', 'category', 'logo']


class MatchLogoWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and hasattr(value, 'url'):
            # Agregamos un estilo CSS para limitar el ancho máximo de la imagen
            output.append(f'<a href="{value.url}" target="_blank"><img src="{value.url}" alt="{name} Logo" style="max-width: 100px; cursor: default; pointer-events: none;" /></a><br>')
        output.append(super().render(name, value, attrs, renderer))
        return mark_safe(''.join(output))
    
class MatchForm(forms.ModelForm):
    local_team_image = forms.ImageField(widget=MatchLogoWidget)
    visiting_team_image = forms.ImageField(widget=MatchLogoWidget)

    date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Match
        fields = ['category', 'date', 'local_team', 'local_team_image', 'local_team_goals', 'visiting_team', 'visiting_team_image', 'visiting_team_goals']