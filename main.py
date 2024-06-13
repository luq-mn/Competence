import discord, dotenv, os, time, datetime
from discord import Option, Embed
os.system("cls")

extensions = ["utilities", "accounts"]

def get_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# IDs to have bot administration
admins = [813939364626169856, 706714932145815614, 871722786006138960]

# Get the token from .env
dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")

time_log = {"start": None, "ready": None}

# Main
if __name__ == "__main__":
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

    # Reload commands
    @bot.slash_command(
        name="reload",
        description="Reload an extension"
    )
    async def reload(
        ctx: discord.ApplicationContext,
        extension: Option(str,"Extension to reload", choices= extensions) #type: ignore
    ):
        if ctx.author.id in admins:
            # Author is listed in admins
            bot.reload_extension(f"commands.{extension}")
            await ctx.respond(
                embed= Embed(
                    title="Extension reload",
                    color=discord.Color.green(),
                    description=f"Reloaded **{extension}** extension",
                )
                .set_footer(text= get_datetime())
            )

        else:
            # Author has no authorize
            await ctx.respond(
                embed= Embed(
                    title="Access denied",
                    color=discord.Color.red(),
                    description= "You are not listed in bot admins."
                )
                .set_footer(text= get_datetime())
            )

    # Run the bot
    bot.run(token)