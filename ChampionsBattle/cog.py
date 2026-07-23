import discord
from discord import app_commands
from discord.ext import commands
from asgiref.sync import sync_to_async

from ChampionsBattle.models import ChampionTeam, PlayerEquippedTeam

class ChampionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /champions
    @app_commands.command(name="champions", description="Champion commands")
    @app_commands.describe(action="equip | current")
    async def champions(self, interaction: discord.Interaction, action: str = "current"):
        await interaction.response.defer(ephemeral=True)

        if action == "equip":
            teams = await sync_to_async(list)(ChampionTeam.objects.filter(is_active=True))
            if not teams:
                await interaction.followup.send("❌ No teams available yet.", ephemeral=True)
                return
            team_list = "\n".join([f"• {t.name}" for t in teams])
            await interaction.followup.send(f"**Available Teams:**\n{team_list}\n\nUse admin panel to equip.", ephemeral=True)

        elif action == "current":
            try:
                equipped = await sync_to_async(PlayerEquippedTeam.objects.get)(player__discord_id=interaction.user.id)
                await interaction.followup.send(f"**Your Current Team:** {equipped.team.name}", ephemeral=True)
            except Exception:
                await interaction.followup.send("❌ You haven't equipped any team yet.", ephemeral=True)

    # /champions_battle start <user>
    @app_commands.command(name="champions_battle", description="Battle commands")
    @app_commands.describe(action="start | add | remove", user="The player you want to battle")
    async def battle(self, interaction: discord.Interaction, action: str, user: discord.User = None):
        await interaction.response.defer(ephemeral=True)

        if action == "start":
            if user is None:
                await interaction.followup.send("❌ Please mention a user: `/champions_battle start @user`", ephemeral=True)
                return

            if user.bot:
                await interaction.followup.send("❌ You cannot battle a bot.", ephemeral=True)
                return

            # Check if user has equipped team
            try:
                await sync_to_async(PlayerEquippedTeam.objects.get)(player__discord_id=user.id)
                await interaction.followup.send(f"⚔️ **Battle started** with **{user}**!", ephemeral=True)
            except Exception:
                await interaction.followup.send(f"❌ **{user}** hasn't equipped a team yet.", ephemeral=True)

        elif action == "add":
            await interaction.followup.send("✅ Added to battle (coming soon).", ephemeral=True)

        elif action == "remove":
            await interaction.followup.send("✅ Removed from battle (coming soon).", ephemeral=True)

        else:
            await interaction.followup.send("Use: `start`, `add`, or `remove`", ephemeral=True)


async def setup(bot):
    await bot.add_cog(ChampionsCog(bot))
    print("✅ ChampionsBattle package loaded successfully!")
