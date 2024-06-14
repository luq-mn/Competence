import discord, dotenv, os, time, datetime
from discord import Option, Embed
os.system("cls")

def get_datetime():
    return f"Timestamp: {datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")} (GMT+8)"

# IDs to have bot administration
admins = [813939364626169856, 706714932145815614, 871722786006138960]

# Get the token from .env
dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")

# Main
if __name__ == "__main__":
    extensions = ["utilities", "accounts"]
    time_log = {"start": None, "ready": None}
    bot = discord.Bot()

    # On bot startup
    time_log["start"] = time.time()
    @bot.event
    async def on_ready():
        # Setting the bot status
        await bot.change_presence(
            status=discord.Status.do_not_disturb,
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="with your life."
            )
        )

        # Logging
        time_log["ready"] = round(time.time() - time_log["start"], 4)
        print(f"Bot logged in as {bot.user} in {time_log['ready']} seconds")
    
    # Load commands
    for extension in extensions:
        bot.load_extension(f"commands.{extension}")

    # Master command
    @bot.slash_command(name="master", description= "Competence master commands")
    async def reload(ctx: discord.ApplicationContext, cmd: Option(str,"Enter master command", required= True)): # type: ignore
        # Check if invoker is an admin
        if ctx.author.id in admins:
            try:
                # Load extension
                if cmd.startswith("load"):
                    _, extension = cmd.split()
                    bot.load_extension(f"commands.{extension}")
                # Reload extension
                elif cmd.startswith("reload"):
                    _, extension = cmd.split()
                    bot.reload_extension(f"commands.{extension}")
                # Unload extension
                elif cmd.startswith("unload"):
                    _, extension = cmd.split()
                    bot.unload_extension(f"commands.{extension}")
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

    # Run the bot
    bot.run(token)