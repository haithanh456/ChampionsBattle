import discord
from discord import app_commands
from discord.ext import commands
from asgiref.sync import sync_to_async

class ChampionsBattleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="champions", description="Champions Battle commands")
    @app_commands.describe(action="What do you want to do?", team="Team name (for equip)")
    @app_commands.choices(action=[
        app_commands.Choice(name="list", value="list"),
        app_commands.Choice(name="equip", value="equip"),
        app_commands.Choice(name="unequip", value="unequip"),
        app_commands.Choice(name="current", value="current"),
    ])
    async def champions(self, interaction: discord.Interaction, action: str, team: str = None):
        from ChampionsBattle.models import ChampionTeam, PlayerEquippedTeam
        from bd_models.models import Player

        await interaction.response.defer(ephemeral=True)

        player, _ = await Player.objects.aget_or_create(discord_id=interaction.user.id)

        if action == "list":
            teams = await sync_to_async(list)(
                ChampionTeam.objects.filter(is_active=True).prefetch_related("balls__ball")
            )
            if not teams:
                await interaction.followup.send("No teams available right now.", ephemeral=True)
                return

            text = "**Available Champion Teams:**\n\n"
            for t in teams:
                ball_names = [b.ball.country for b in t.balls.all()]
                balls_text = ", ".join(ball_names) if ball_names else "No balls yet"
                text += f"**{t.name}**\n→ {balls_text}\n\n"

            await interaction.followup.send(text, ephemeral=True)

        elif action == "equip":
            if not team:
                await interaction.followup.send("Please type the team name.", ephemeral=True)
                return

            try:
                chosen_team = await ChampionTeam.objects.prefetch_related("balls__ball").aget(
                    name__iexact=team, is_active=True
                )
            except ChampionTeam.DoesNotExist:
                await interaction.followup.send("That team does not exist or is not active.", ephemeral=True)
                return

            # Equip the team
            await PlayerEquippedTeam.objects.aupdate_or_create(
                player=player,
                defaults={"team": chosen_team}
            )

            ball_names = [b.ball.country for b in chosen_team.balls.all()]
            balls_text = ", ".join(ball_names) if ball_names else "No balls"

            await interaction.followup.send(
                f"✅ You equipped **{chosen_team.name}**!\n"
                f"Borrowed balls: {balls_text}\n\n"
                f"These balls are temporary — you can only use them, you don't own them.",
                ephemeral=True
            )

        elif action == "unequip":
            deleted, _ = await PlayerEquippedTeam.objects.filter(player=player).adelete()
            if deleted:
                await interaction.followup.send("You unequipped your team.", ephemeral=True)
            else:
                await interaction.followup.send("You don't have any team equipped.", ephemeral=True)

        elif action == "current":
            try:
                equipped = await PlayerEquippedTeam.objects.select_related("team").prefetch_related(
                    "team__balls__ball"
                ).aget(player=player)
                ball_names = [b.ball.country for b in equipped.team.balls.all()]
                balls_text = ", ".join(ball_names) if ball_names else "No balls"
                await interaction.followup.send(
                    f"You currently have **{equipped.team.name}** equipped.\n"
                    f"Balls: {balls_text}",
                    ephemeral=True
                )
            except PlayerEquippedTeam.DoesNotExist:
                await interaction.followup.send("You don't have any team equipped.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ChampionsBattleCog(bot))
