import discord
from discord import Embed

# def info(ctx):
#     embed = (
#         Embed(
#             title= "Bot info",
#             description= "An overview of the bot",
#             color= discord.Color.blue()
#         )
#         .add_field(name= "Total servers", value= len(ctx.bot.guilds), inline= True)
#         .add_field(name= "Total users", value= len(ctx.bot.users), inline= True)
#     )

#     return embed

def ping(ctx):
    embed = (
        Embed(
            title= ":ping_pong: Pong!",
            description= f"I fucked your mother {round(ctx.bot.latency * 1000)} milliseconds ago",
            color= discord.Color.blue()
        )
    )

    return embed
