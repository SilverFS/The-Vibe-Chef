import discord
from discord import Embed
import os, os.path
from discord.ext import commands
import requests
import random



class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(name="meme",
                      description="Use this command to display a random meme video.",
                      brief="A command for a random meme video.")
    async def meme(self, ctx, arg=""):
        r = requests.get('https://cdn.shiruvaaa.net/')
        count = int(r.text) - 1
        if arg == "":
            await ctx.send(f'https://cdn.shiruvaaa.net/{random.randint(1, count)}.mp4')
        else:
            try:
                if int(arg) in range(1, count):
                    await ctx.send(f'https://cdn.shiruvaaa.net/{arg}.mp4')
                else:
                    await ctx.send(f"The video does not exist. (try using the numbers 1 till {count})")
            except:
                await ctx.send(f"Numbers, you bumbling idiot! (try using the numbers 1 till {count})")
        






    @commands.Cog.listener()
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.bot.user:
            return

        #personal request :)
        if message.author.id == 245889377421623297 and 'q' in message.content:
            await message.channel.send("Cool story brah, *Drags balls across screen *", tts=True)





        list = ['vibecheck', 'vibe check', 'penis boter jelly tijd', 'vibe']
        if message.content in list:
            if message.content == list[2]:
                responses = ['Whatever floats your boat, man.',
                         '*MOANS *',
                         'ERROR: WEIRD VIBES DETECTED.',
                         'COOL VIBES YO, *DRAGS BALLS ACROSS SCREEN *']
            

            else:
                responses = ['VIBE!',
                            'VIBING',
                            'STILL VIBING',
                            'VIBING HARD!',
                            'VIBING EVEN HARDER!',
                            'FEELING THE VIBES!',
                            'CALCULATING VIBES...',
                            'NO VIBES FOUND.. SAD LIFE :(',
                            'ERROR: no vibes found.']
           
            
            vibeResponse = ((f'{random.choice(responses)}'))
            await message.channel.send(vibeResponse) ##(f'> {random.choice(responses)}')             
            


    



#Defines class as cog
def setup(bot):
    bot.add_cog(Fun(bot))