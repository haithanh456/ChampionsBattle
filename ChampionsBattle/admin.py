from django.contrib import admin
from .models import ChampionTeam, ChampionTeamBall

class ChampionTeamBallInline(admin.TabularInline):
    model = ChampionTeamBall
    extra = 1
    autocomplete_fields = ("ball",)

@admin.register(ChampionTeam)
class ChampionTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_editable = ("is_active",)
    inlines = [ChampionTeamBallInline]
