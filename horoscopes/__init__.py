from .horoscopes import Horoscopes


def setup(bot):
    bot.add_cog(Horoscopes())