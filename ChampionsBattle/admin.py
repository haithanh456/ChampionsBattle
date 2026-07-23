from django.contrib import admin
from .models import ChampionTeam, ChampionTeamBall, PlayerEquippedTeam

class ChampionTeamBallInline(admin.TabularInline):
    model = ChampionTeamBall
    extra = 1
    autocomplete_fields = ("ball",)
    ordering = ("order",)

@admin.register(ChampionTeam)
class ChampionTeamAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name",)
    list_editable = ("is_active",)
    inlines = [ChampionTeamBallInline]

@admin.register(PlayerEquippedTeam)
class PlayerEquippedTeamAdmin(admin.ModelAdmin):
    list_display = ("player", "team", "equipped_at")
    search_fields = ("player__discord_id", "team__name")
    autocomplete_fields = ("player", "team")
