import discord
from discord import Embed

def server_join(guild):
    embed = (
        Embed(
            title= "Someone accidentally pressed Join",
            color= discord.Color.brand_green()
        )
        .add_field(name= "Name", value= guild.name)
        .add_field(name= "ID", value= guild.id)
        .add_field(name= "Creator", value= guild.owner.mention)
        .add_field(name= "Dumb People", value= guild.member_count)
        .add_field(name= "Subscriptions", value= len(guild.roles))
        .add_field(name= "Channels", value= len(guild.channels))

        .set_footer(text= "why would they join this ass server lmao")
    )

    return embed

def server_leave(guild):
    embed = (
        Embed(
            title= "Good riddance",
            color= discord.Color.brand_red()
        )
        .add_field(name= "The asshole", value= guild.name)
        .add_field(name= "ID", value= guild.id)
        .add_field(name= "Creator", value= guild.owner.mention)
        .add_field(name= "Dumb fucks", value= guild.member_count)
        .add_field(name= "Subscriptions", value= len(guild.roles))
        .add_field(name= "Channels", value= len(guild.channels))

        .set_footer(text= "Nobody liked you")
    )

    return embed

def cog_reload(cog):
    embed= (
        Embed(
            title= "Bot is shitting in its hands and smearing it on the screen",
            description= f"{cog} has been smeared successfully",
            color= discord.Color.brand_green()
        )
        .set_footer(text= "Something new is coming?")
    )

    return embed

def code_error(error):
    embed= (
        Embed(
            title= "Error",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "you fucked up boyo")
    )

    return embed

def command_not_found(error):
    embed= (
        Embed(
            title= "Command not found",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "Are you stupid")
    )

    return embed

def command_on_cooldown(error):
    embed= (
        Embed(
            title= "Get off that command brotha",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "Not yet brotha")
    )

    return embed

def command_missing_arguments(error):
    embed= (
        Embed(
            title= "Missing arguments",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "Betta go argue bitch")
    )

    return embed

def command_missing_permissions(error):
    embed= (
        Embed(
            title= "Missing permissions",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "Imagine not having permissions :skull:")
    )

    return embed

def command_bot_missing_permissions(error):
    embed= (
        Embed(
            title= "Bot missing permissions",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "I don't have the permissions required to make this happen :(")
    )

    return embed
