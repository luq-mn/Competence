import discord, json, os
import scripts.embeds as embeds
from discord.ext import commands

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("config.json", "r") as f:
            self.config = json.load(f)
        self.server_channel = self.bot.get_channel(self.config["logs"]["servers"])

    @discord.slash_command(name ="master", description = "Competence master commands")
    async def reload(self,ctx: discord.ApplicationContext, cmd: discord.Option(str,"Enter master command", required= True)): # type: ignore
        # Check if invoker is an admin
        if ctx.author.id in self.config["admins"]:
            try:
                # Pull from repo
                if cmd.startswith("pull"):
                    os.system("git pull")
                    await ctx.respond(embed = embeds.Master.pull())
                
                # Bot info
                elif cmd.startswith("info"):
                    await ctx.respond(embed = embeds.Master.info(ctx))

                # Load extension
                elif cmd.startswith("load"):
                    _, extension = cmd.split()
                    self.bot.load_extension(f"scripts.cogs.{extension}")
                    await ctx.respond(embed = embeds.Master.load())

                # Reload extension
                elif cmd.startswith("reload"):
                    _, extension = cmd.split()
                    # Reload all extensions
                    if extension == "all":
                        for extension in self.config["extensions"]:
                            self.bot.reload_extension(f"scripts.cogs.{extension}")
                        await ctx.respond(embed = embeds.Master.reload())

                    # Reload a specific extension
                    else:
                        self.bot.reload_extension(f"scripts.cogs.{extension}")
                        await ctx.respond(embed = embeds.Master.reload())

                # Unload extension
                elif cmd.startswith("unload"):
                    _, extension = cmd.split()
                    self.bot.unload_extension(f"scripts.cogs.{extension}")
                    await ctx.respond(embed = embeds.Master.unload())

                # No such command
                else:
                    await ctx.respond(embed = embeds.Master.not_found())

            # Error
            except Exception as err:
                await ctx.respond(embed = embeds.Master.error(err))

        # Author is not an admin
        else:
            # Author has no authorize
            await ctx.respond(embed = embeds.Master.unauthorize())

def setup(bot):
    bot.add_cog(Master(bot))