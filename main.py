import discord, dotenv, os, time, datetime
from discord import Option, Embed
os.system("cls")

def get_datetime():
    return f"""Timestamp: {datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")} (GMT+8)"""

# IDs to have bot administration
admins = [813939364626169856, 706714932145815614, 871722786006138960]

# Get the token from .env
dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")

# Main
if __name__ == "__main__":
    extensions = ["utilities", "accounts", "master"]
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

    # Run the bot
    bot.run(token)