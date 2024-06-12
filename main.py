import discord, dotenv, os, time
os.system("cls")

# Get the token from .env
dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")

# Time logs
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
    bot.load_extension("commands.utilities")

    bot.run(token) # Run the bot