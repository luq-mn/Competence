import discord, json, os
import scripts.embeds as embeds
from discord.ext import commands

from backend import statistics
st = statistics.StatisticsTracker()

from backend.accounts import AccountManager
am = AccountManager()

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Get the channel specified in config.json
        with open("./config.json", "r") as f:
            self.config = json.load(f)
        self.server_channel = self.bot.get_channel(self.config["logs"]["servers"])

    @discord.slash_command(name ="master", description = "Competence master commands")
    async def reload(self,ctx: discord.ApplicationContext, cmd: discord.Option(str,"Enter master command", required= True)): # type: ignore
        locked = am.check_lock(ctx.author.id)
        if locked:
            await ctx.respond(embed = embeds.Accounts.lock_locked(), ephemeral=True)
        else:
            # Check if invoker is an admin
            if ctx.author.id in self.config["admins"]:
                try:
                    # Pull from repo
                    if cmd.startswith("pull"):
                        os.system("git pull")
                        await ctx.respond(embed = embeds.Master.pull())
                        st.command_log(ctx.author.id, "pull", "success", round(self.bot.latency * 1000))
                        st.event_log("pull", "success")
                    
                    # Bot info
                    elif cmd.startswith("info"):
                        await ctx.respond(embed = embeds.Master.info(ctx))
                        st.command_log(ctx.author.id, "info", "success", round(self.bot.latency * 1000))

                    # Add everyone to bot database
                    elif cmd.startswith("members"):
                        for guild in ctx.bot.guilds:
                            for member in guild.members:
                                am.check_exists(member.id)

                    # Set user account flag

                    # Reset database (owner only - luq.mn)

                    # Close bot
                    elif cmd.startswith("close"):
                        await self.bot.close()

                    # Load extension
                    elif cmd.startswith("load"):
                        _, extension = cmd.split()
                        self.bot.load_extension(f"scripts.cogs.{extension}")
                        await ctx.respond(embed = embeds.Master.load())
                        st.command_log(ctx.author.id, "load", extension, round(self.bot.latency * 1000))
                        st.event_log("load", extension)

                    # Reload extension
                    elif cmd.startswith("reload"):
                        _, extension = cmd.split()
                        # Reload all extensions
                        if extension == "all":
                            for extension in self.config["extensions"]:
                                self.bot.reload_extension(f"scripts.cogs.{extension}")
                            await ctx.respond(embed = embeds.Master.reload())
                            st.command_log(ctx.author.id, "reload", "all", round(self.bot.latency * 1000))
                            st.event_log("reload", "all")

                        # Reload a specific extension
                        else:
                            self.bot.reload_extension(f"scripts.cogs.{extension}")
                            await ctx.respond(embed = embeds.Master.reload())
                            st.command_log(ctx.author.id, "reload", extension, round(self.bot.latency * 1000))
                            st.event_log("reload", extension)

                    # Unload extension
                    elif cmd.startswith("unload"):
                        _, extension = cmd.split()
                        self.bot.unload_extension(f"scripts.cogs.{extension}")
                        await ctx.respond(embed = embeds.Master.unload())
                        st.command_log(ctx.author.id, "unload", extension, round(self.bot.latency * 1000))
                        st.event_log("unload", extension)

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