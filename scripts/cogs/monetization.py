import discord
from discord.ext import commands
import scripts.embeds as embeds

class Monetization(commands.Cog):
    @discord.slash_command(name = "transfer", description = "Transfer money to another user")
    async def account(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Monetization())
