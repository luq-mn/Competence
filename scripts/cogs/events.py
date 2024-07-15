import discord, json, os
from discord.ext import commands
import scripts.embeds as embeds

from backend import statistics
st = statistics.StatisticsTracker()

from backend.accounts import AccountManager
am = AccountManager()

with open("./config.json", "r") as f:
    config = json.load(f)

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.bot.get_channel(config["logs"]["servers"])
        await channel.send(embed= embeds.Events.server_join(guild))
        st.event_log("server join", guild.id)

        # Loop through all server members and check if account exists
        for member in guild.members:
            am.check_exists(member.id)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(config["logs"]["servers"])
        await channel.send(embed= embeds.Events.server_leave(guild))
        st.event_log("server leave", guild.id)

def setup(bot):
    bot.add_cog(Events(bot))