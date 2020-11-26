from redbot.core import commands
import aiohttp


class ImBored(commands.Cog):
    """Gives you activities to do when bored. Credits: http://www.boredapi.com"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def imbored(self, ctx):
        """Suggests some activities for you to do when bored."""
        async with aiohttp.request("GET", "http://www.boredapi.com/api/activity/") as r:
            results = await r.json()
        activity = results["activity"]
        em = discord.Embed(description=activity)
        await ctx.send(embed=em)