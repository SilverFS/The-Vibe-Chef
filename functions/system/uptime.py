import discord
from discord import Embed
from discord.ext import commands
import os
import requests
import dns.resolver

requests.adapters.DEFAULT_RETRIES = 20


class checker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="urlwatch",
                brief="URL check tool",
                description="use '%urlwatch <argument>' to check if a website is up or down.")
    async def urlwatch(self, ctx, arg):
        url = (f"http://{arg}") 
        urlEmbed = discord.Embed(title=(f"{arg} is: "), description="Up!", color=0x992d22)
        urlEmbed2 = discord.Embed(title=(f"{arg} is: "), description="Down!", color=0x992d22)
        #Gets status here
        try:
            req = requests.get(url)
            status = (req.status_code == 200)
        except:
            status = False
        if status == True:
            await ctx.send(embed=urlEmbed)
        else:
            await ctx.send(embed=urlEmbed2)



    

        
        
#Defines class as cog
def setup(bot):
    bot.add_cog(checker(bot))