from .cog import ChampionsCog

async def setup(bot):
    await bot.add_cog(ChampionsCog(bot))
