import discord
from discord.ext import commands
import scripts.embeds as embeds

class Accounts(commands.Cog):
    @discord.slash_command(name = "account", description = "Account overview")
    async def account(self, ctx):
        pass

    @discord.slash_command(name = "lock", description = "Toggle account usability")
    async def balance(self, ctx):
        pass

    @discord.slash_command(name = "settings", description = "Account settings")
    async def balance(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Accounts())
