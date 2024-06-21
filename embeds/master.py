import discord
from discord import Embed

class MasterEmbeds:
    def __init__(self, bot):
        self.bot = bot
    
    def ping(self, latency):
        embed = (Embed(
            title= "Pong!",
            description= f"Gets the latency of the bot.",
            color= discord.Color.blue()
        )
        .add_field(name= "Latency", value= f"{latency}ms", inline= True)

        .set_footer(text= f"Requested by {self.bot.user.name}", icon_url= self.bot.user.avatar_url)
        .timestamp()
        )
  
        return embed
    
    def reload(extension, status):
        if status: # Authorised
            embed= (Embed(
                title= "Extension reload",
                description= f"The extension {extension} has been reloaded.",
                color= discord.Color.brand_green()
            )
            .set_footer(text= "Admin only command")
            .timestamp()
            )
            return embed
        
        elif status == False: # Not authorised
            embed= (Embed(
                title= "Extension reload",
                description= f"You are not authorised to use this command.",
                color= discord.Color.brand_red()
            )
            .set_footer(text= "Admin only command")
            .timestamp()
            )
            return embed
        
        else: # 
            embed= (Embed(
                title= "Extension reload",
                description= status
            )
            .set_footer(text= "Admin only command")
            .timestamp()
            )
            return embed