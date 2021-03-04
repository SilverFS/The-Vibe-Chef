import discord
from discord import Embed
from discord.ext import commands
import platform #For stats


class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
 

    ##Basic ping function (with embed)
    @commands.command(name="ping", 
                    brief="Show's the chef's latency in ms.", 
                    description="Use this command if you want to know what my latency is!",
                    usage="`ping`")
    async def ping(self, ctx):
        bot = self.bot
        pong = ((f":ping_pong: {round(bot.latency * 1000)}ms"))
        myembed = discord.Embed(title=pong, color=0x992d22)
        await ctx.send(embed=myembed)



    ##Stats command
    @commands.command(name="stats", 
                      brief="The statistics of the bot.", 
                      description="Statistics of the bot includes: discord.py version, Python version and how many servers the bot is in.")
    async def stats(self, ctx):
      bot = self.bot
      pythonVersion = platform.python_version()
      dpyVersion = discord.__version__
      serverCount = len(bot.guilds)
      memberCount = len(set(bot.get_all_members()))
      desResult = (f"I'm in {serverCount} servers, with a total of {memberCount} members. :blush:\nI'm running python {pythonVersion} and discord.py {dpyVersion} :snake:")
      myembed = discord.Embed(title="My current stats:", description=desResult, color=0xf1c40f)
      await ctx.send(embed=myembed)






#Defines class as cog
def setup(bot):
    bot.add_cog(Utilities(bot))