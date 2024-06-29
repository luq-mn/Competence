import discord
from discord.ext import commands
import scripts.embeds as embeds

from backend import statistics
st = statistics.StatisticsTracker()

class Joos(commands.Cog):
    @discord.slash_command(name = "joos", description = "Get joos")
    async def account(self, ctx):
        await ctx.respond(embed= embeds.Joos.joos())
        st.command_log(ctx.author.id, "joos", f"{round(ctx.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Joos())
