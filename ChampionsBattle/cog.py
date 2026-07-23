import discord
from discord import app_commands
from discord.ext import commands
from django.utils import timezone
from asgiref.sync import sync_to_async

class ChampionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /champions equip
    @app_commands.command(name="champions", description="Equip a champion team")
    @app_commands.describe(action="equip | current")
    async def champions(self, interaction: discord.Interaction, action: str = "current"):
        await interaction.response.defer(ephemeral=True)

        if action == "equip":
            teams = await sync_to_async(list)(ChampionTeam.objects.filter(is_active=True))
            if not teams:
                await interaction.followup.send("❌ No teams available yet.", ephemeral=True)
                return

            team_list = "\n".join([f"• {t.name} [{t.get_category_display()}]" for t in teams])
            await interaction.followup.send(f"**Available Teams:**\n{team_list}\n\nUse admin panel to equip a team for now.", ephemeral=True)

        elif action == "current":
            try:
                equipped = await sync_to_async(PlayerEquippedTeam.objects.get)(player__discord_id=interaction.user.id)
                await interaction.followup.send(f"**Your Current Team:** {equipped.team.name}", ephemeral=True)
            except Exception:
                await interaction.followup.send("❌ You haven't equipped any team yet.", ephemeral=True)

    # /champions battle start
    @app_commands.command(name="champions_battle", description="Battle commands")
    @app_commands.describe(action="start | add | remove", user="Opponent for battle")
    async def battle(self, interaction: discord.Interaction, action: str, user: discord.User = None):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send("⚔️ Battle system coming soon!", ephemeral=True)


    @app_commands.command(name="sync", description="Sync commands")
    async def sync(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await self.bot.tree.sync()
        await interaction.followup.send("✅ Commands synced!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(ChampionsCog(bot))
    print("✅ ChampionsBattle package loaded successfully!")
