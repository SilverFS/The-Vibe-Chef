import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import platform #For stats
import json

class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
 

    ##Basic ping function (with embed)
    @commands.command(name="ping",
                    help="Use this command if you want to know what my latency is!",
                    brief="Show's the chef's latency in ms.", 
                    description="Use this command if you want to know what my latency is!",
                    usage="`ping`")
    async def ping(self, ctx):
        bot = self.bot
        pong = ((f":ping_pong: {round(bot.latency * 1000)}ms"))
        myembed = discord.Embed(title=pong, color=0x992d22)
        await ctx.send(embed=myembed)



    ##Stats command
    @commands.command(aliases=['statistics', 'status'],
                      name="stats",
                      help="Statistics of the bot includes: discord.py version, Python version and how many servers the bot is in.",
                      brief="The statistics of the bot.", 
                      description="Statistics of the bot includes: discord.py version, Python version and how many servers the bot is in.")
    async def stats(self, ctx):
      bot = self.bot


      pythonVersion = platform.python_version()
      dpyVersion = discord.__version__
      serverCount = len(bot.guilds)
      desResult = (f"I'm currently checking vibes in {serverCount} servers :blush:\nI'm running Python {pythonVersion} and discord.py {dpyVersion} :snake:\n")
      myembed = discord.Embed(title="My current stats:", description=desResult, color=0xf1c40f)
      myembed.set_footer(icon_url = ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
      myembed.set_author(name='The Vibe-Chef',
      icon_url='https://cdn.discordapp.com/avatars/771763476946878484/3f51758747ce8752edb25811afa61f5a.png?size=4096')
      await ctx.send(embed=myembed)




    ##Sets custom prefix for each server
    @commands.command(aliases=['customprefix', 'prefix'],
                      name="setprefix",
                      brief="Custom prefix for your server", 
                      description="Sets the prefix of your favourite bot in your own server.")
    @commands.has_permissions(administrator=True)                  
    async def setprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.message.guild.id)] = prefix

        #dumps all prefixes in the json file
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent = 4)
            await ctx.send(f"Great! You can now call this awesome bot with your new prefix: {prefix}")
            
        
    @setprefix.error
    async def ksetprefix_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You have insufficient vibes for this command.")



#Defines class as cog
def setup(bot):
    bot.add_cog(Utilities(bot))