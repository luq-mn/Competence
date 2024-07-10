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
        locked = am.check_lock(ctx.author.id)
        if locked:
            await ctx.respond(embed = embeds.Accounts.lock_locked())
        else:
            await ctx.respond("WIP")

    @discord.slash_command(name = "lock", description = "Toggle account usability")
    async def lock(self, ctx, password: discord.Option(str, description= "Enter password, default is 'password'", required= False, default= "password")): #type: ignore
        lock = am.toggle_lock(ctx.author.id, password)

        if lock == "unlocked":
            await ctx.respond(embed = embeds.Accounts.lock_unlocked())
            st.command_log(ctx.author.id, "/lock", "unlocked", round(ctx.bot.latency * 1000))

        elif lock == "enabled":
            await ctx.respond(embed = embeds.Accounts.lock_enabled())
            st.command_log(ctx.author.id, "/lock", "locked", round(ctx.bot.latency * 1000))

        elif lock == "wrong password":
            await ctx.respond(embed = embeds.Accounts.lock_wrong_password())
            st.command_log(ctx.author.id, "/lock", "wrong password", round(ctx.bot.latency * 1000))

    @discord.slash_command(name = "settings", description = "Account settings")
    async def settings(self, ctx):
        locked = am.check_lock(ctx.author.id)
        if locked:
            await ctx.respond(embed = embeds.Accounts.lock_locked())
        else:
            await ctx.respond("WIP")

def setup(bot):
    bot.add_cog(Accounts())
