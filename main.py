import discord, os, time
from dotenv import load_dotenv
os.system("cls")

#Token loading
load_dotenv(".env")
TOKEN = str(os.getenv("TOKEN"))

#Bot script
if __name__ == "__main__":
    bot = discord.Bot(
        intents= discord.Intents.all()
    )

    #Startup config
    startup_time = time.time()
    @bot.event
    async def on_ready():
        #Bot status
        await bot.change_presence(
            status= discord.Status.online,
            activity= discord.Activity(
                type= discord.ActivityType.playing,
                name= "Well? /help"
            )
        )

        startup_duration = round(time.time() - startup_time, 4)
        print(f"{bot.user} is online, time taken: {startup_duration}s\n")

    #Cogs - Loading the scripts
    bot.load_extension("scripts.modules.tools")

    bot.run(TOKEN)