import discord
import scripts.embeds as embeds
from discord.ext import commands

#Backend
# from backend.accounts import AccountManager
# am = AccountManager()
# from backend.statistics import StatisticsTracker
# st = StatisticsTracker()

#Commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Ping
    @discord.slash_command(name="ping", description="Get the bot latency")
    async def ping(self, ctx: discord.ApplicationContext):
        # Get the bot latency
        await ctx.respond(embed= embeds.General.ping(ctx))

def setup(bot):
    bot.add_cog(General(bot))