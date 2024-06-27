from typing import Any
from discord import Embed, Color, __version__

class General:
    def ping(ctx):
        embed = (
            Embed(
                title = ":ping_pong: Pong!",
                description = f"Latency: {round(ctx.bot.latency * 1000)}ms",
                color = Color.blue()
            )
            .set_footer(text= "A command all bots have tbh")
        )
        return embed

class Master:
    def info(ctx):
        embed = (
            Embed(
                title= "Bot info",
                description= "General bot info",
                color= Color.blue()
            )
            .add_field(name= "Bot name", value= ctx.bot.user.name, inline= True)
            .add_field(name= "Bot ID", value= ctx.bot.user.id, inline= "True")
            .add_field(name= "\u200b", value= "\u200b")
            .add_field(name= "Servers", value= len(ctx.bot.guilds), inline= True)
            .add_field(name= "Users", value= len(ctx.bot.users), inline= True)
            .add_field(name= "\u200b", value= "\u200b")
            .add_field(name= "Commands", value= len(ctx.bot.commands), inline= True)
            .add_field(name= "Pycord version", value= __version__, inline= True)
            .add_field(name= "\u200b", value= "\u200b")

            .set_footer(text= "Basic things about the bot")
        )
        return embed

    def pull():
        embed = (
            Embed(
                title= "Pulled from GitHub repo",
                description= "Code pulled from the Competence repo",
                color= Color.brand_green()
            )
            .set_footer(text= "This thing pulls")
        )
        return embed

    def load():
        embed = (
            Embed(
                title= "Load extension",
                description= "Extension loaded successfully.",
                color= Color.brand_green()
            )
            .set_footer(text= "Something new")
        )
        return embed
    
    def unload():
        embed = (
            Embed(
                title= "Unload extension",
                description= "Extension unloaded successfully.",
                color= Color.brand_green()
            )
            .set_footer(text= "Goodbye"
            )
        )
        return embed
    
    def reload():
        embed = (
            Embed(
                title= "Reload extension",
                description= "Extension reloaded successfully.",
                color= Color.brand_green()
            )
            .set_footer(text= "Refreshed")
        )
        return embed
    
    def not_found():
        embed = (
            Embed(
                title= "Command not found",
                description= "This command does not exist, or maybe you fucked up a parameter?",
                color= Color.brand_red()
            )
            .set_footer(text= "womp womp")
        )
        return embed

    def error(err):
        embed = (
            Embed(
                title= "Error",
                description= err,
                color= Color.brand_red()
            )
            .set_footer(text= "Something went wrong")
        )
        return embed
    
    def unauthorised():
        embed = (
            Embed(
                title = "Unathorized",
                description= "You are not authorised to use this command.",
                color= Color.brand_red()
            )
            .set_footer(text= "Imagine having permissions 💀")
        )
        return embed
    
class Events:
    def server_join(guild):
        embed = (
            Embed(
                title= "Bot joined a new server",
                color= Color.brand_green()
            )
            .add_field(name= "Server name", value= guild.name, inline= True)
            .add_field(name= "Server ID", value= guild.id, inline= True)
            .add_field(name= "\u200b", value= "\u200b")
            .add_field(name= "Server channels", value= len(guild.channels), inline= True)
            .add_field(name= "Server members", value= len(guild.members), inline= True)
            .add_field(name= "\u200b", value= "\u200b")

            .set_footer(text= "Something new ig")
        )
        return embed
    
    def server_leave(guild):
        embed = (
            Embed(
                title= "Bot left a server",
                color= Color.brand_red()
            )
            .add_field(name= "Server name", value= guild.name, inline= True)
            .add_field(name= "Server ID", value= guild.id, inline= True)
            .add_field(name= "\u200b", value= "\u200b")
            .add_field(name= "Server channels", value= len(guild.channels), inline= True)
            .add_field(name= "Server members", value= len(guild.members), inline= True)
            .add_field(name= "\u200b", value= "\u200b")

            .set_footer(text= "buh bye")
        )
        return embed