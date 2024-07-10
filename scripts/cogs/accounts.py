import discord
from discord.ext import commands
import scripts.embeds as embeds

from backend.statistics import StatisticsTracker
st = StatisticsTracker()

from backend.accounts import AccountManager
am = AccountManager()

class Accounts(commands.Cog):
    @discord.slash_command(name = "account", description = "Account overview")
    async def account(self, ctx):
        pass

    @discord.slash_command(name = "lock", description = "Toggle account usability")
    async def balance(self, ctx, password: discord.Option(str, description= "Enter password, default is 'password'", required= False, default= "password")): #type: ignore
        lock = am.toggle_lock(ctx.author.id, password)

        if lock == "unlocked":
            await ctx.respond(embeds = embeds.Accounts.lock("unlocked"))
            st.command_log(ctx.author.id, "/lock", "unlocked", round(self.bot.latency() * 1000))

        elif lock == "locked":
            await ctx.respond(embeds = embeds.Accounts.lock("locked"))
            st.command_log(ctx.author.id, "/lock", "locked", round(self.bot.latency() * 1000))

        elif lock == "wrong password":
            await ctx.respond(embeds = embeds.Accounts.lock("wrong password"))
            st.command_log(ctx.author.id, "/lock", "wrong password", round(self.bot.latency() * 1000))

    @discord.slash_command(name = "settings", description = "Account settings")
    async def balance(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Accounts())
