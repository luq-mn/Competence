import discord, json, os
from discord.ext import commands
import scripts.embeds as embeds

from backend import statistics
st = statistics.StatisticsTracker()

with open("./config.json", "r") as f:
    config = json.load(f)

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(config["logs"]["servers"])
        await channel.send(embed= embeds.Events.server_join(guild))
        st.bot_log("another one fell for that big green join button, we gettin rich tonight", guild.id)
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(config["logs"]["servers"])
        await channel.send(embed= embeds.Events.server_leave(guild))
        st.bot_log("we lost one. we'll make it i'm sure", guild.id)

def setup(bot):
    bot.add_cog(Events(bot))
