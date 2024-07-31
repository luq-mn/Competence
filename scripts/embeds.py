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
            .set_footer(text= "This thing pulls you")
        )
        return embed

    def load():
        embed = (
            Embed(
                title= "extend Yourself",
                description= "Extension loaded successfully.",
                color= Color.brand_green()
            )
            .set_footer(text= "Adjustments may require a reboot to apply.")
        )
        return embed
    
    def unload():
        embed = (
            Embed(
                title= "Unload Unload Unload Unload Unload",
                description= "Extension unloaded.",
                color= Color.brand_green()
            )
            .set_footer(text= "Goodbye"
            )
        )
        return embed
    
    def reload():
        embed = (
            Embed(
                title= "reLoad Yourself",
                description= "Extension reloaded successfully.",
                color= Color.brand_green()
            )
            .set_footer(text= "Adjustments may take 1-2 days to apply.")
        )
        return embed
    
    def not_found():
        embed = (
            Embed(
                title= "not Found",
                description= "you Messed up, Robert",
                color= Color.brand_red()
            )
            .set_footer(text= "you Messed up you Messed up you Messed up you Messed up you Messed up you Messed up you Messed up you Messed up")
        )
        return embed

    def error(err):
        embed = (
            Embed(
                title= "Uh Oh",
                description= err,
                color= Color.brand_red()
            )
            .set_footer(text= "you Messed up")
        )
        return embed
    
    def unauthorised():
        embed = (
            Embed(
                title = "Unauthorized",
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
    
class Joos:
    def joos():
        embed = (
            Embed(
                title= "Joos solves issues",
                description= "<:joos:1256553567410720853>"
            )
            .set_footer(text= "cope")
        )
        return embed

class Accounts:
    def account():
        embed = (
            Embed(
                title= "Account overview",
                color= Color.blue()
            )
        )
        return embed
    
    def lock_disabled():
        embed = (
                Embed(
                    title= "Account unlocked",
                    description= "Your account has been unlocked successfully",
                    color= Color.brand_green()
                )
                .set_footer(text= "Monetization access is now enabled")
            )
        return embed
    
    def lock_enabled():
        embed = (
                Embed(
                    title= "Account locked",
                    description= "Your account has been locked successfully",
                    color= Color.brand_green()
                )
                .set_footer(text= "Monetization access is now disabled")
            )
        return embed
    
    def lock_wrong_password():
        embed = (
                Embed(
                    title= "Invalid password",
                    description= "The password you entered is incorrect",
                    color= Color.brand_red()
                )
                .add_field(name= "I forgot my password!", value= "Join the discord server, and contact an admin to help you out.", inline= True)
                
                .set_footer(text= "womp womp")
            )
        return embed
    
    def lock_locked():
        embed = (
                Embed(
                    title= "This account is locked",
                    description= "Your account is locked, supposedly by you, as a security measure.",
                    color= Color.brand_red()
                )
                .add_field(name= "How to unlock", value= "Use the `/lock [password]` command to unlock your account.", inline= True)
                .add_field(name= "I frogor my password!", value= "Join the discord server, and contact an admin to help you out.", inline= True)

                .set_footer(text= "Womp womp go unlock it")
            )
        return embed
