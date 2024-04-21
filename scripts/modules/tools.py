import discord
from discord import ApplicationContext, Option, Embed
from discord.ext import commands
from discord.ext.commands import Cog

class Tools(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Ping
    @discord.slash_command(
        name= "ping",
        description= "Pings the bot, returns latency in ms."
    )
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)

        await ctx.respond(
            embed= Embed(
                description= f"> Bot Latency\n {latency}ms"

            )
            .set_author(name= "Pong!")
            .set_footer(text= "Competence Discord bot")
        )
    
def setup(bot):
    bot.add_cog(Tools(bot))