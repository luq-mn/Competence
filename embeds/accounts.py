import discord
from discord import Embed

class AccountEmbeds:
    def __init__(self, bot):
        self.bot = bot

    # Initialise account
    def initialise(self, ctx, initialised: bool):
        if initialised: # Account initialised
            embed = (Embed(
                title= "Account initialisation",
                description= f"{ctx.author.mention}'s account has been manually initialised.",
                color= discord.Color.brand_green()
            )
            .set_footer(text= "You are now part of the system!")
            .timestamp()
            )
            return embed
        
        else: # Account already exists
            embed = (Embed(
                title= "Account initialisation",
                description= f"Failed to initialise, {ctx.author.mention}'s account already exists.",
                color= discord.Color.brand_red()
            )
            .set_footer(text= "You are already in the system lol")
            .timestamp()
            )
            return embed

    # Overview
    def overview(self, ctx, flag, tier, access, xp):
        embed = (Embed(
            title= "Account overview",
            description= f"{ctx.author.mention}'s account overview.",
            color= discord.Color.light_gray()
        )
        .add_field(name= "Flag", value= flag, inline= True)
        .add_field(name= "Tier", value= tier, inline= True)
        .add_field(name= "\u200b", value= "\u200b")
        .add_field(name= "Access", value= access, inline= True)
        .add_field(name= "XP", value= xp, inline= True)

        .set_footer(text= "A glimpse of your account")
        .timestamp()
        )

    # Reset account
    def reset(self, author):
        pass
