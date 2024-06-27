import discord
from discord.ext import commands
import scripts.embeds as embeds

class Accounts(commands.Cog):
    @discord.slash_command(name = "account", description = "Overview of your account")
    async def account(self, ctx):
        pass

    @discord.slash_command(name = "lock", description = "Toggle ability to perform actions on your account")
    async def balance(self, ctx):
        pass

    @discord.slash_command(name = "settings", description = "Settings for your account")
    async def balance(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Accounts())