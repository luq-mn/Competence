import discord, json
from discord.ext import commands
import scripts.embeds as embeds

with open("config.json", "r") as f:
    config = json.load(f)

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_guild_join(self, guild):
            channel = self.bot.get_channel(config["logs"]["servers"])
            await channel.send(embed= embeds.Events.server_join())
        
        @commands.Cog.listener()
        async def on_guild_remove(self, guild):
            channel = self.bot.get_channel(config["logs"]["servers"])
            await channel.send(embed= embeds.Events.server_leave())

def setup(bot):
    bot.add_cog(Events(bot))