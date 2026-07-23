from django.db import models
from bd_models.models import Ball

class ChampionTeam(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Champion Team"
        verbose_name_plural = "Champion Teams"

class ChampionTeamBall(models.Model):
    team = models.ForeignKey(ChampionTeam, on_delete=models.CASCADE, related_name="balls")
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team.name} - {self.ball.country}"

    class Meta:
        verbose_name = "Team Ball"
        verbose_name_plural = "Team Balls"
