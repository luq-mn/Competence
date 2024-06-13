import discord, datetime
from discord import ApplicationContext, Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

from backend.statistics import StatisticsTracker
stats = StatisticsTracker()

from backend.accounts import AccountManager
am = AccountManager()

class Accounts(Cog):
    def __init__(self, bot):
        self.bot = bot

        account = bot.create_group("account", "Manage your account")

        @account.command(
            name= "overview",
            description= "An overview of your account"
        )
        async def overview(
            ctx,
            user: Option(discord.User, "The user to get an overview of", required=False) # type: ignore
        ):
            if not user:
                user = ctx.author

            await ctx.respond(
                embed= Embed(
                    title= f"{user.name} Account Overview",
                    color= discord.Color.blue()
                )
                .add_field(
                    name= "Bank balance", value= f""
                )
            )
        
        @account.command(
            name= "init",
            description= "Initialize your account"
        )
        async def initialise(ctx):
            if am.initialise(ctx.author.id):
                # Account already exists
                await ctx.respond(
                    embed= Embed(
                        title= "Account already exists",
                        color= discord.Color.red()
                    )
                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, "account init", "User already has account")

            else:
                # Initialise account
                await ctx.respond(
                    embed= Embed(
                        title= "Account initialised",
                        color= discord.Color.green()
                    )
                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, "account init", "initialised")
        
        @account.command(
            name= "balance",
            description= "Get your account balance"
        )
        async def balance(ctx):
            if not am.get_balance(ctx.author.id):
                # Account does not exist
                await ctx.respond(
                    embed= Embed(
                        title= "Account does not exist",
                        color= discord.Color.red()
                    )
                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, "account balance", "Account does not exist")

            else:
                # Get balance
                balance = am.get_balance(ctx.author.id)
                await ctx.respond(
                    embed= Embed(
                        title= "Account balance",
                        color= discord.Color.green()
                    )
                    .add_field(
                        name= "Balance", value= balance
                    )
                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, "account balance", "Account balance")

# Setup cog            
def setup(bot):
    bot.add_cog(Accounts(bot))