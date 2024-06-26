from discord import Embed, Color

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
                color = Color.brand_green()
            )
            .set_footer(text= "Something new")
        )
        return embed
    
    def unload():
        embed = (
            Embed(
                title= "Unload extension",
                description= "Extension unloaded successfully.",
                color = Color.brand_green()
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
                color = Color.brand_green()
            )
            .set_footer(text= "Refreshed")
        )
        return embed
    
    def not_found():
        embed = (
            Embed(
                title= "Command not found",
                description= "This command does not exist, or maybe you fucked up a parameter?",
                color = Color.brand_red()
            )
            .set_footer(text= "womp womp")
        )
        return embed

    def error(err):
        embed = (
            Embed(
                title= "Error",
                description= err,
                color = Color.brand_red()
            )
            .set_footer(text= "Something went wrong")
        )
        return embed
    
    def unauthorised():
        embed = (
            Embed(
                title= "Unathorized",
                description= "You are not authorised to use this command.",
                color = Color.brand_red()
            )
            .set_footer(text= "Imagine having permissions 💀")
        )
        return embed