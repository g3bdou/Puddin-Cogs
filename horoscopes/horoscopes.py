from redbot.core import commands
import pyaztro


class Horoscopes(commands.Cog):
    """Gives infos about your horoscope sign. Credits: Pyaztro"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def horoscope(self, ctx, sign: str):
        try:
            horoscope = pyaztro.Aztro(sign=sign)
        except:
            await ctx.send("`{}` is not a sign.".format(sign))
            return

        date1 = horoscope.date_range[0]
        em = discord.Embed(title="{} :{}:".format(sign.upper(), sign), description="**:scroll: Description:** {}\n**:zany_face: Mood:** {}\n**:timer: Lucky Time:** {}\n**:art: Lucky Color:** {}\n**:game_die: Lucky Number:** {}\n**:fingers_crossed: Compatibility:** {} :{}:".format(horoscope.description, horoscope.mood, horoscope.lucky_time, horoscope.color, horoscope.lucky_number, horoscope.compatibility, horoscope.compatibility.lower()), color=discord.Color(0xa216e9))
        date1 = horoscope.date_range[0]
        date2 = horoscope.date_range[1]
        date_range = "DATE RANGE: {} - {}".format(date1.strftime("%x"), date2.strftime("%x"))
        em.set_footer(text=date_range)
        await ctx.send(embed=em)