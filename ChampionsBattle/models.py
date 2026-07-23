from django.db import models
from bd_models.models import Ball, Player

class ChampionTeam(models.Model):
    CATEGORY_CHOICES = [
        ("attack", "Attack"),
        ("defense", "Defense"),
        ("speed", "Speed"),
        ("support", "Support"),
        ("balanced", "Balanced"),
        ("legendary", "Legendary"),
    ]

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="balanced")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} [{self.get_category_display()}]"

    class Meta:
        verbose_name = "Champion Team"
        verbose_name_plural = "Champion Teams"

class ChampionTeamBall(models.Model):
    team = models.ForeignKey(ChampionTeam, on_delete=models.CASCADE, related_name="balls")
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE)
    bonus_percent = models.PositiveIntegerField(default=0)  # +0% by default

    def __str__(self):
        return f"{self.team.name} - {self.ball.country} (+{self.bonus_percent}%)"

class PlayerEquippedTeam(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, unique=True)
    team = models.ForeignKey(ChampionTeam, on_delete=models.CASCADE)
    equipped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player} - {self.team.name}"

    class Meta:
        verbose_name = "Player Equipped Team"
        verbose_name_plural = "Player Equipped Teams"
