import discord, json
import embeds.master as embeds
from discord.ext import bridge, commands

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("config.json", "r") as f:
            self.log_channels = json.load(f)["log"]
        self.server_channel = self.bot.get_channel(self.log_channels["servers"])

    @bridge.BridgeExtCommand
    async def reload(self, ctx: bridge.BridgeContext, cog: str):
        try:
            self.bot.reload_extension(cog)
            await ctx.respond(embed= embeds.cog_reload(cog))
        except Exception as err:
            await ctx.respond(embed= embeds.code_error(err), ephemeral= True)

def setup(bot):
    bot.add_cog(Master(bot))