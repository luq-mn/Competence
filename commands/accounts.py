import discord, datetime
from discord import ApplicationContext, Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

from main import get_datetime

from backend.accounts import AccountManager
am = AccountManager()

from backend.statistics import StatisticsTracker
stats = StatisticsTracker()

# Main Class
class Accounts(Cog):
    def __init__(self, bot):
        self.bot = bot

        # User command group
        user = bot.create_group("account", "Everything related to an account.")

        @user.command(
            name= "init",
            description= "Initializes your account"
        )
        async def initliase(ctx: ApplicationContext):
            status = am.account_check(ctx.author.id)
            if status:
                await ctx.respond(
                    embed= Embed(
                        title= "Account already exists",
                        color= discord.Color.red()
                    )
                    .set_footer(text= get_datetime())
                )
                stats.command_log(ctx.author.id, "account init", "Account already exists")

            else:
                await ctx.respond(
                    embed= Embed(
                        title= "Account initialized",
                        color= discord.Color.green()
                    )
                    .set_footer(text= get_datetime())
                )
                stats.command_log(ctx.author.id, "account init", "Account initialized")

# Setup Cog
def setup(bot):
    bot.add_cog(Accounts(bot))