import discord
from discord import ApplicationContext, Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

from backend.statistics import StatisticsTracker
stats = StatisticsTracker()

# Main Class
class Utilities(Cog):
    def __init__(self, bot):
        self.bot = bot
    
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
            .set_footer(text= f"Invoked by {ctx.author.name}")
        )
        stats.command_invoked(ctx.author.id, ctx.guild.id, "ping", f"{latency}ms")

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
            .set_footer(text= f"Invoked by {ctx.author.name}")
        )
        stats.command_invoked(ctx.author.id, ctx.guild.id, "calculator", f"{var} = {eval(var)}")

# Setup Cog
def setup(bot):
    bot.add_cog(Utilities(bot))