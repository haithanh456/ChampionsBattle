from django.contrib import admin
from .models import ChampionTeam

@admin.register(ChampionTeam)
class ChampionTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_editable = ("is_active",)
