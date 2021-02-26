import discord
from discord import Embed
from discord.ext import commands
import platform #For stats

import dns.resolver



class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    
    @commands.command(name="dns",
                brief="A simple DNS lookup tool!",
                description="A simple DNS lookup tool.")
    async def dnsname(self, ctx, arg):
        HOST = (arg)
        a_record = dns.resolver.query(HOST, 'A', raise_on_no_answer=False)
        aaaa_record = dns.resolver.query(HOST, 'AAAA', raise_on_no_answer=False)
        cname_record = dns.resolver.query(HOST, 'CNAME', raise_on_no_answer=False)
        mx_record = dns.resolver.query(HOST, 'MX', raise_on_no_answer=False)
        ns_record = dns.resolver.query(HOST, 'NS', raise_on_no_answer=False)
        

        dnsArray = ['**A**', '**AAAA**', '**CNAME**', '**MX**', '**NS**']
        counter = 0
        totalMessage = ""
        
        for qtype in [a_record, aaaa_record, cname_record, mx_record, ns_record]:
            totalMessage += dnsArray[counter]
            counter += 1
            totalMessage += ("\n")
            for answer in qtype:
                totalMessage += (f"{answer}")
                totalMessage += ("\n")
            totalMessage += ("_______\n")
        dnsEmbed = discord.Embed(title=(f"Lookup results for: {HOST}"), description=totalMessage, color=0x992d22)
        await ctx.send(embed=dnsEmbed)


        






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
    @commands.command(name="stats", brief="The statistics of the bot.", description="Statistics of the bot includes: discord.py version, Python version and how many servers the bot is in.")
    async def stats(self, ctx):
      bot = self.bot
      pythonVersion = platform.python_version()
      dpyVersion = discord.__version__
      serverCount = len(bot.guilds)
      memberCount = len(set(bot.get_all_members()))
      statsresult = ((f"My current stats:\n \nI'm in {serverCount} servers, with a total of {memberCount} members. :blush:\nI'm running python {pythonVersion} and discord.py {dpyVersion} :snake:"))
      myembed = discord.Embed(title=statsresult, color=0xf1c40f)
      await ctx.send(embed=myembed)









#Defines class as cog
def setup(bot):
    bot.add_cog(Utilities(bot))