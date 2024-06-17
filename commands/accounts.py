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
        account = bot.create_group("account", "Everything related to an account.")

        @account.command(
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
        
        @account.command(
                name= "overview",
                description= "An overview of your account"
        )
        async def overview(ctx: ApplicationContext):
            balance = am.account_balance(ctx.author.id)
            details = am.account_tier(ctx.author.id)

            await ctx.respond(
                embed= Embed(
                    title= "Account overview",
                    description= f"Overview of {ctx.author.mention}'s account",
                    color= discord.Color.green()
                )
                .add_field(name= "Balance", value= f"${balance}")
                .add_field(name= "Tier", value= details["tier"])

                .set_footer(text= get_datetime())
            )
            stats.command_log(ctx.author.id, "account overview", f"Account overviewed for {ctx.author.name}")
            

        @account.command(
                name= "balance",
                description= "Check your account's balance"
        )
        async def balance(ctx: ApplicationContext):
            balance = am.account_balance(ctx.author.id)

            await ctx.respond(
                embed= Embed(
                    title= "Account balance",
                    description= f"Current account balance of {ctx.author.mention}",
                    color= discord.Color.green()
                )
                .add_field(name= "Balance", value= f"${balance}")
                .set_footer(text= get_datetime())
            )
            stats.command_log(ctx.author.id, "account balance", f"Account balance: ${balance}")

        @account.command(
            name= "transfer",
            description= "Transfer money to another user"
        )
        async def transfer(
            ctx: ApplicationContext,
            user: Option(discord.Member, description= "Select a user", required= True), # type: ignore
            amount: Option(float, description= "Enter amount", required= True), # type: ignore
            note: Option(str, description= "Add note to this transaction", required= False) # type: ignore
        ):
            if note == None:
                note = "No description provided."

            status = am.account_transfer(ctx.author.id, user.id, amount, note)
            if status == "success":
                await ctx.respond(
                    embed= Embed(
                        title= "Transfer successful",
                        description= "No issues found.",
                        color= discord.Color.green()
                    )
                    .add_field(name= "Recipient", value= user.mention, inline= True)
                    .add_field(name= "Amount", value= f"${amount}", inline= True)
                    .add_field(name= "\u200b", value= "\u200b")
                    .add_field(name= "Note", value= note)

                    .set_footer(text= get_datetime())
                )
                stats.command_log(ctx.author.id, "account transfer", f"${amount} transferred to ${user}")

            elif status == "exceed":
                await ctx.respond(
                    embed= Embed(
                        title= "Transfer failed",
                        description= "The amount you are transferring exceeds your transfer limit.",
                        color= discord.Color.red()
                    )
                    .add_field(name= "Recipient", value= user.mention, inline= True)
                    .add_field(name= "Amount", value= f"${amount}", inline= True)
                    .add_field(name= "\u200b", value= "\u200b")
                    .add_field(name= "Note", value= note)

                    .set_footer(text= get_datetime())
                )
                stats.command_log(ctx.author.id, "account transfer", f"Transaction failed: amount exceeds transfer limit")
                
            elif status == "insufficient":
                await ctx.respond(
                    embed= Embed(
                        title= "Transfer failed",
                        description= "Insufficient balance to perform transaction with the provided amount.",
                        color= discord.Color.red()
                    )
                    .add_field(name= "Recipient", value= user.mention, inline= True)
                    .add_field(name= "Amount", value= f"${amount}", inline= True)
                    .add_field(name= "\u200b", value= "\u200b")
                    .add_field(name= "Note", value= note)

                    .set_footer(text= get_datetime())
                )
                stats.command_log(ctx.author.id, "account transfer", f"Transaction failed: insufficient balance")

# Setup Cog
def setup(bot):
    bot.add_cog(Accounts(bot))