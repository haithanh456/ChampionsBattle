from django.db import models
from bd_models.models import Ball, Player

class ChampionTeam(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Champion Team"
        verbose_name_plural = "Champion Teams"

class ChampionTeamBall(models.Model):
    team = models.ForeignKey(ChampionTeam, on_delete=models.CASCADE, related_name="balls")
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.ball.country}"

    class Meta:
        verbose_name = "Team Ball"
        verbose_name_plural = "Team Balls"
        ordering = ["order"]

class PlayerEquippedTeam(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="equipped_team")
    team = models.ForeignKey(ChampionTeam, on_delete=models.CASCADE)
    equipped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player} → {self.team.name}"

    class Meta:
        verbose_name = "Player Equipped Team"
        verbose_name_plural = "Player Equipped Teams"
