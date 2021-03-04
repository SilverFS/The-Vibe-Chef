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

        
        
#Defines class as cog
def setup(bot):
    bot.add_cog(checker(bot))