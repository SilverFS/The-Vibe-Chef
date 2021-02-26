import discord
from discord import Embed
from discord.ext import commands



class modulescmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def load (self, ctx, extension):
        self.bot.load_extension(f'functions.{extension}')

    @commands.command()
    async def unload (self, ctx, extension):
        self.bot.unload_extension(f'functions.{extension}')

    @commands.command()
    async def reload (self, ctx, extension):
        self.bot.unload_extension(f'functions.{extension}')
        self.bot.load_extension(f'functions.{extension}')


#Defines class as cog
def setup(bot):
    bot.add_cog(modulescmd(bot))









    