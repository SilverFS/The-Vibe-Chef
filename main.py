import discord
from discord import Embed
import glob, os, json
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp, __version__
intents = discord.Intents.all()
def test_version():
    assert __version__ == "1.1.0"


#custom get_prefix
def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    #returns all Server ID's
    return prefixes[str(message.guild.id)]







menu=DefaultMenu(page_left='⬅️', page_right='➡️', remove='🗑️')

# Custom ending note
ending_note = "Output of the command: {help.clean_prefix}{help.invoked_with}. Use an extra parameter to get detailed information."
            #"The ending note from {ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"

#Defines initial prefix and pretty_help command
bot = commands.Bot(command_prefix= get_prefix, case_insensitive=True)
bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note, author_id = 296302114794373121, color=discord.Color.gold(), active_time=60, show_index=False, intents = intents, sort_commands=True)






##Adds guild to json file
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '%'

    #dumps all prefixes in the json file
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)


##Removes guild from json file
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    #pops the string of server id
    prefixes.pop(str(guild.id))

    #dumps all prefixes in the json file
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)



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
bot.run(token)