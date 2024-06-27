import discord
from discord.ext import commands
import scripts.embeds as embeds

from backend import statistics
st = statistics.StatisticsTracker()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping
    @discord.slash_command(name = "ping", description = "Get the bot latency")
    async def ping(self, ctx: discord.ApplicationContext):
        # Get the bot latency
        await ctx.respond(embed= embeds.General.ping(ctx))
        st.command_log(ctx.author.id, "ping", f"{round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(General(bot))