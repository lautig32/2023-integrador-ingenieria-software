from django.contrib import admin

from .models import *

admin.site.register(Club)
admin.site.register(Person)
admin.site.register(FootballCategory)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(PlayerSuspension)