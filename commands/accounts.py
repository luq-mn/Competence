import discord, datetime
from discord import ApplicationContext, Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

from backend.statistics import StatisticsTracker
stats = StatisticsTracker()

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

            await ctx.send(
                embed= Embed(
                    title= f"{user.name} Account Overview",
                    color= discord.Color.blue()
                )
                .add_field(
                    name= "Bank balance", value= f""
                )
            )

def setup(bot):
    bot.add_cog(Accounts(bot))