import discord
from discord import Embed
import glob, os
from discord.ext import commands
from pretty_help import Navigation, PrettyHelp, __version__
def test_version():
    assert __version__ == "1.1.0"




#Defines prefix and pretty_help command
bot = commands.Bot(
	command_prefix="%", case_insensitive=True, help_command=PrettyHelp(navigation=Navigation(page_left='⬅️', page_right='➡️', remove='🗑️'), color=discord.Color.gold(), active=60, sort_commands=True))
bot.author_id = 296302114794373121  #Author discord ID!!!



#Prints in console
@bot.event 
async def on_ready():
  serverCount = len(bot.guilds)
  print(f'Logged in as {bot.user.name} - {bot.user.id}')
  #bot.remove_command('help')
  await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{serverCount} Servers\n | %help", inline="False"))

# Load up modules from modules folder
for filename in glob.iglob('functions/**/*.py', recursive=True):
    module = filename.replace('.py', '').replace(os.sep, '.')
    print(f'Loaded module {module}')
    bot.load_extension(module)

#Token to get the bot up and going
token = os.environ.get("DISCORD_BOT_SECRET") #It's in another file :P
bot.run(token)  # Starts the bot