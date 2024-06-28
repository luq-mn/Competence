import discord
from discord.ext import commands
import scripts.embeds as embeds

class Accounts(commands.Cog):
    @discord.slash_command(name = "account", description = "Account Overview")
    async def account(self, ctx):
        pass

    @discord.slash_command(name = "lock", description = "Toggle Account Usability")
    async def balance(self, ctx):
        pass

    @discord.slash_command(name = "settings", description = "Account Settings")
    async def balance(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Accounts())
