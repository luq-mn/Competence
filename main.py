import discord, dotenv, os

# Get the token from .env
dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="hello", description="Say hello!")
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run(token)