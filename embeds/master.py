import discord
from discord import Embed

def server_join(guild):
    embed = (
        Embed(
            title= "Added to new server",
            color= discord.Color.brand_green()
        )
        .add_field(name= "Name", value= guild.name)
        .add_field(name= "ID", value= guild.id)
        .add_field(name= "Owner", value= guild.owner.mention)
        .add_field(name= "Members", value= guild.member_count)
        .add_field(name= "Roles", value= len(guild.roles))
        .add_field(name= "Channels", value= len(guild.channels))

        .set_footer(text= "A new journey awaits")
    )

    return embed

def server_leave(guild):
    embed = (
        Embed(
            title= "Left server",
            color= discord.Color.brand_red()
        )
        .add_field(name= "Name", value= guild.name)
        .add_field(name= "ID", value= guild.id)
        .add_field(name= "Owner", value= guild.owner.mention)
        .add_field(name= "Members", value= guild.member_count)
        .add_field(name= "Roles", value= len(guild.roles))
        .add_field(name= "Channels", value= len(guild.channels))

        .set_footer(text= "Sad to see this one go")
    )

    return embed

def cog_reload(cog):
    embed= (
        Embed(
            title= "Cog reload",
            description= f"'{cog}' cog has been reloaded successfully",
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
        .set_footer(text= "Something went wrong")
    )

    return embed

def command_not_found(error):
    embed= (
        Embed(
            title= "Command not found",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "That does NOT exist")
    )

    return embed

def command_on_cooldown(error):
    embed= (
        Embed(
            title= "Command on cooldown",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "Not yet brother")
    )

    return embed

def command_missing_arguments(error):
    embed= (
        Embed(
            title= "Missing arguments",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "Gotta be complete bruh")
    )

    return embed

def command_missing_permissions(error):
    embed= (
        Embed(
            title= "Missing permissions",
            description= error,
            color= discord.Color.brand_red()
        )
        .set_footer(text= "You are not allowed to use that one!")
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