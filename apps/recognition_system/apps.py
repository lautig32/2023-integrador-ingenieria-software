from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class RecognitionSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.recognition_system'
    verbose_name = _('Recognition System')
