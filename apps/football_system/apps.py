from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FootballSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.football_system'
    verbose_name = _('Football System')
