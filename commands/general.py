import discord
import embeds.general as embeds
from discord.ext import bridge, commands

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
    @bridge.BridgeExtCommand
    async def ping(self, ctx: bridge.BridgeContext):
        # Get the bot latency
        await ctx.respond(embed= embeds.ping(ctx))

def setup(bot):
    bot.add_cog(General(bot))