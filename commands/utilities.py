import discord, datetime
from discord import ApplicationContext, Option, Embed
from discord.ext.commands import Cog

from main import get_datetime

from backend.statistics import StatisticsTracker
stats = StatisticsTracker()

# Main Class
class Utilities(Cog):
    def __init__(self, bot):
        self.bot = bot

        # User command group
        user = bot.create_group("user", "Commands related to a user")

        @user.command(
            name= "info",
            description= "Get info of a user"
        )
        async def user_info(ctx, member: Option(discord.User, description= "User to get info of", required= False)): # type: ignore
            if member == None:
                member = ctx.author
            
            await ctx.respond(
                embed= Embed(
                    title= member.name,
                    color= discord.Color.green(),
                    description= "Basic information about the user."
                )
                .add_field(name= "Nickname", value= member.display_name, inline= True)
                .add_field(name= "ID", value= member.id, inline= True)
                .add_field(name= "\u200b", value= "\u200b")
                .add_field(name= "Joined server (UTC)", value= member.joined_at, inline= True)
                .add_field(name= "Created account (UTC)", value= member.created_at, inline= True)
                .add_field(name= "\u200b", value= "\u200b")
                .add_field(name= "Roles", value= len(member.roles), inline= True)

                .set_footer(text= get_datetime())
            )
            stats.command_log(ctx.author.id, "user info", 
                f"Nickname: {member.display_name}, ID: {member.id}, Joined server (UTC): {member.joined_at}, Created account (UTC): {member.created_at}, Roles: {len(member.roles)}"
            )

    # Ping
    @discord.slash_command(
        name= "ping",
        description= "Pings the bot to check its latency"
    )
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.respond(
            embed= Embed(
                title= ":ping_pong: Pong!",
                color= discord.Color.green(),
                description= f"Latency: {latency}ms"
            )
            .set_footer(text= get_datetime())
        )
        stats.command_log(ctx.author.id, "ping", f"Latency: {latency}ms")

    # Calculator
    @discord.slash_command(
        name= "calculator",
        description= "Basic math operations"
    )
    async def calculator(
        self,
        ctx: ApplicationContext,
        num1: Option(str, description= "Number to perform operation"), # type: ignore
        operation: Option(str, choices=["+", "-", "*", "/", "**"]), # type: ignore
        num2: Option(str, description= "Second number to perform operation on with the first number"), # type: ignore
    ):
        var = f"{num1} {operation} {num2}"
        await ctx.respond(
            embed= Embed(
                title= "Calculator",
                color= discord.Color.green(),
                description= f"Result: {var} = {eval(var)}"
            )
            .set_footer(text= get_datetime())
        )
        stats.command_log(ctx.author.id, "calculator", f"{var} = {eval(var)}")

# Setup Cog
def setup(bot):
    bot.add_cog(Utilities(bot))