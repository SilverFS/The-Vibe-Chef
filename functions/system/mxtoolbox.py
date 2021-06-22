import discord
from discord import Embed
from discord.ext import commands
import os
import requests
import dns.resolver

requests.adapters.DEFAULT_RETRIES = 20


class MXToolbox(commands.Cog):

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

        
        
#Defines class as cog
def setup(bot):
    bot.add_cog(MXToolbox(bot))