import discord, json
import embeds.master as embeds
from discord.ext import commands

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("config.json", "r") as f:
            self.config = json.load(f)
        self.server_channel = self.bot.get_channel(self.config["logs"]["servers"])

    @discord.slash_command(name="master", description= "Competence master commands")
    async def reload(self,ctx: discord.ApplicationContext, cmd: discord.Option(str,"Enter master command", required= True)): # type: ignore
        # Check if invoker is an admin
        if ctx.author.id in self.config["admins"]:
            try:
                # Load extension
                if cmd.startswith("load"):
                    _, extension = cmd.split()
                    self.bot.load_extension(f"commands.{extension}")
                # Reload extension
                elif cmd.startswith("reload"):
                    _, extension = cmd.split()
                    self.bot.reload_extension(f"commands.{extension}")
                # Unload extension
                elif cmd.startswith("unload"):
                    _, extension = cmd.split()
                    self.bot.unload_extension(f"commands.{extension}")
                # Not such command
                else:
                    await ctx.respond(f"{cmd} is not a valid command. Maybe you fucked up a parameter?")
                    return
                # Success
                await ctx.respond("Master command executed successfully.")
            except Exception as err:
                # Error
                await ctx.respond(f"**Error**: {err}")
        else:
            # Author has no authorize
            await ctx.respond("You are not authorised to use this command.")

def setup(bot):
    bot.add_cog(Master(bot))