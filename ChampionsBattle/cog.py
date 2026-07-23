import discord
from discord import app_commands
from discord.ext import commands

class ChampionsBattleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="champions", description="Champions Battle system")
    async def champions(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Champions Battle is ready!\nCommands will be added soon.",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(ChampionsBattleCog(bot))
