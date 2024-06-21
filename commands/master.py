import discord
from discord.ext import commands

from embeds.master import MasterEmbeds


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping
    @commands.command(name= "ping")
    async def ping(self, ctx, *, message: str):
        await ctx.send(embed= MasterEmbeds.ping(self.bot.latency * 1000))

    # Reload extension
    @commands.command(name= "reload")
    async def reload(self, ctx, *, extension: str):
        try:
            self.bot.reload_extension(f"commands.{extension}")
            await ctx.send(MasterEmbeds.reload(extension, True))
        except Exception as err:
            await ctx.send(MasterEmbeds.reload(err))


# import discord, datetime, subprocess
# from discord import ApplicationContext, Option, Embed
# from discord.ext import commands
# from discord.ext.commands import Cog

# from main import get_datetime, admins

# # Backend
# from backend.accounts import AccountManager
# am = AccountManager()
# from backend.statistics import StatisticsTracker
# stats = StatisticsTracker()

# # Main Class
# class Master(Cog):
#     def __init__(self, bot):
#         @bot.slash_command(name="master", description= "Competence master commands (admin only)")
#         async def reload(ctx: discord.ApplicationContext, cmd: Option(str,"Enter command to execute", required= True)): # type: ignore
#             # Check if invoker is an admin
#             if ctx.author.id in admins:
#                 try:
#                     # System commands
#                     # if cmd.startswith("pull"):
#                     #     _, command = cmd.split()
#                     #     output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
#                     #     await ctx.respond(output)
#                     #     return
#                     if cmd.startswith("ping"):
#                         latency = round(bot.latency * 1000)
#                         await ctx.respond(
#                             embed= Embed(
#                                 title= ":ping_pong: Pong!",
#                                 color= discord.Color.green(),
#                                 description= f"Latency: {latency}ms"
#                             )
#                             .set_footer(text= get_datetime())
#                         )
#                         stats.command_log(ctx.author.id, "ping", f"Latency: {latency}ms")
                    
#                     # Extension commands
#                     elif cmd.startswith("load"):
#                         _, extension = cmd.split()
#                         bot.load_extension(f"commands.{extension}")
#                     elif cmd.startswith("reload"):
#                         _, extension = cmd.split()
#                         bot.reload_extension(f"commands.{extension}")
#                     elif cmd.startswith("unload"):
#                         _, extension = cmd.split()
#                         bot.unload_extension(f"commands.{extension}")

#                     # Command does not exist
#                     else:
#                         await ctx.respond(f"{cmd} is not a valid command. Maybe you fucked up a parameter?")
#                         return
#                     # Success
#                     await ctx.respond("Master command executed successfully.")
#                 except Exception as err:
#                     # Error
#                     await ctx.respond(f"**Error**: {err}")
#             else:
#                 # Author has no authorize
#                 await ctx.respond("You are not authorised to use this command.")
        
#         @bot.command()

# # Setup Cog
# def setup(bot):
#     bot.add_cog(Master(bot))