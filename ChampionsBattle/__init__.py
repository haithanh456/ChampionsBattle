async def setup(bot):
    from .cog import ChampionsBattleCog
    await bot.add_cog(ChampionsBattleCog(bot))
