import discord
from discord import Embed, FFmpegPCMAudio
import os, os.path
from os import listdir
from os.path import isfile, join
from discord.ext import commands
import requests
import random
from discord.voice_client import VoiceClient
import asyncio
from discord.utils import get



class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(name="meme",
                      description="Use this command to display a random meme video from a personal database.",
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
                await ctx.send(f"Use numbers, you bumbling idiot! (try using the numbers 1 till {count})")
        


    @commands.command(name="moan",
                      description="Use this command to do let the chef say something in voice chat...",
                      brief="A command for a random moan.")
    async def moan(self, ctx):
        bot = self.bot
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)

        path = 'functions/media/audio/moans/'
        #path = 'functions\\media\\audio\\moans\\'
        list = [f for f in listdir(path) if isfile(join(path, f))]



        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            await ctx.send(":weary: :hot_face:")
            voice = await channel.connect()
            print(f"The bot has moaned in: {channel}\n")
            

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(path + random.choice(list))
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
        while voice_client.is_playing():
            await asyncio.sleep(0.5)
        await voice.disconnect()



    @commands.command(name="theboys",
                      description="Use this command to display a random meme video.",
                      brief="No description needed.")
    async def theboys(self, ctx):
        bot = self.bot
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)

        path = 'functions/media/audio/boys/'
        #path = 'functions\\media\\audio\\boys\\'
        onlyaudio = [f for f in listdir(path) if isfile(join(path, f))]

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"The bot vibed with the boys in: {channel}\n")

        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(path + random.choice(onlyaudio))
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
        while voice_client.is_playing():
            await asyncio.sleep(0.5)
        await voice.disconnect()



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