import discord
from discord import app_commands
from discord.ext import commands

class ChampionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="champions", description="Champion commands")
    @app_commands.describe(action="equip | current")
    async def champions(self, interaction: discord.Interaction, action: str = "current"):
        if action == "equip":
            await interaction.response.send_message("**Available Teams:**\nUse admin panel to equip a team.", ephemeral=True)
        elif action == "current":
            await interaction.response.send_message("You haven't equipped any team yet.", ephemeral=True)
        else:
            await interaction.response.send_message("Use: `/champions equip` or `/champions current`", ephemeral=True)

    @app_commands.command(name="champions_battle", description="Battle commands")
    @app_commands.describe(action="start | add | remove")
    async def battle(self, interaction: discord.Interaction, action: str):
        await interaction.response.send_message("⚔️ Battle system coming soon!", ephemeral=True)

    @app_commands.command(name="sync", description="Sync commands")
    async def sync(self, interaction: discord.Interaction):
        await interaction.response.send_message("✅ Commands synced!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(ChampionsCog(bot))
    print("✅ ChampionsBattle package
