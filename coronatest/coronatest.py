from redbot.core import commands
from random import randint
import asyncio


class CoronaTest(commands.Cog):
    """Tests someone for corona virus. (for fun)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coronatest(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.message.author
        
        msg = await ctx.send(":test_tube: **Testing {} for COVID-19 :microbe:**".format(member.mention))
        await asyncio.sleep(1)
        await msg.edit(content=":thermometer: **Testing {}'s temperature**".format(member.mention))
        await asyncio.sleep(2)
        await msg.edit(content=":dna: **Testing {}'s DNA**".format(member.mention))
        await asyncio.sleep(2)
        await msg.edit(content=":microscope: **Analyzing {}'s test results...**".format(member.mention))
        await asyncio.sleep(3)
        await msg.edit(content="**{}'s test results**".format(member.mention))

        if random.randint(1, 100) > 50:
            tem = round(random.uniform(37.2, 42.2), 1)
            dna = ":a:"
            covid = random.randint(10, 100)
            em = discord.Embed(description="{} **tested Positive :heavy_plus_sign: for COVID-19 :microbe:**".format(member.mention), color=discord.Color(0xff0000))
            em.add_field(name="Details :bar_chart:", value=":thermometer: **Temperature:** {}°C\n:dna: **DNA type:** {}\n :microbe: **COVID-19:** {}%".format(tem, dna, covid))
            await msg.edit(embed=em)
        else:
            tem = round(random.uniform(36.1, 37.2), 1)
            dna = random.choice([":regional_indicator_t:", ":regional_indicator_c:", ":regional_indicator_g:"])
            covid = round(random.uniform(0.1, 1), 1)
            em = discord.Embed(description="{} **tested Negative :heavy_minus_sign: for COVID-19 :microbe:**".format(member.mention), color=discord.Color(0x12ec46))
            em.add_field(name="Details :bar_chart:", value=":thermometer: **Temperature:** {}°C\n:dna: **DNA type:** {}\n :microbe: **COVID-19:** {}%".format(tem, dna, covid))
            await msg.edit(embed=em)