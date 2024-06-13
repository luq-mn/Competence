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
                # Initialise account
                await ctx.respond(
                    embed= Embed(
                        title= "Account initialised",
                        color= discord.Color.green()
                    )
                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, "account init", "initialised")

            else:
                # Account already exists
                await ctx.respond(
                    embed= Embed(
                        title= "Account already exists",
                        color= discord.Color.red()
                    )
                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, "account init", "User already has account")
        
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

        @account.command(
            name= "transfer",
            description= "Transfer money to another user"
        )
        async def transfer(
            ctx,
            user: Option(discord.User, "The user to transfer to", required=True), # type: ignore
            amount: Option(int, "The amount to transfer", required=True), # type: ignore
            description: Option(str, "The description of the transfer", required=False) # type: ignore
        ):
            if description == None:
                description = "No description provided"

            if am.transfer(ctx.author.id, user.id, amount, description):
                # Transfer successful
                await ctx.respond(
                    embed= Embed(
                        title= "Transfer successful",
                        color= discord.Color.green()
                    )
                    .add_field(name= "Sender", value= ctx.author.name)
                    .add_field(name= "Receiver", value= user.name)
                    .add_field(name= "\u200b", value= "\u200b")
                    .add_field(name= "Amount", value= amount)
                    .add_field(name= "Description", value= description)

                    .set_footer(text= f"Invoked by {ctx.author.name}")
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, 
                    "account transfer", f"Transfer successful from {ctx.author.name} to {user.name} amount: {amount}"
                )
            
            else:
                # Transfer failed
                await ctx.respond(
                    embed= Embed(
                        title= "Transfer failed",
                        color= discord.Color.red(),
                        description= "Transfer failed. Recipient/Sender may not have an account initialised, or not enough balance."
                    )
                )
                stats.command_invoked(ctx.author.id, ctx.guild.id, 
                    "account transfer", f"Transfer failed from {ctx.author.name} to {user.name} amount: {amount}"
                )

# Setup cog            
def setup(bot):
    bot.add_cog(Accounts(bot))