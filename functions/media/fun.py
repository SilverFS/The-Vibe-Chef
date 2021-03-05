import discord
from discord import Embed
import os, os.path
from discord.ext import commands
import random



class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(name="meme",
                      help="Use this command to display a random meme video.",
                      brief="A command for a random meme video.",
                      description="Use this command to display a random meme video.")
    async def meme(self, ctx, arg=""):
        count = 0
        d = "D:\\IT-DATA\\PROJECTS\\Coding\\The Vibe-chef Discord bot\\functions\\media\\videos" #Your directory here
        for path in os.listdir(d):
            if os.path.isfile(os.path.join(d, path)):
                count += 1
        if arg == "":
            await ctx.send(file=discord.File(f'{d}\\{random.randint(1, count)}.mp4'))
        else:
            try:
                await ctx.send(file=discord.File(f'{d}\\{arg}.mp4'))
            except:
                await ctx.send(f"The video does not exist. (try using the numbers 1 till {count})")






    @commands.Cog.listener()
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.bot.user:
            return

        
        if message.content == 'vibecheck':
            responses = ['VIBE!',
                         'VIBING',
                         'STILL VIBING',
                         'VIBING HARD!',
                         'VIBING EVEN HARDER!']
            vibeResponse = ((f'{random.choice(responses)}'))
            await message.channel.send(vibeResponse) ##(f'> {random.choice(responses)}')             
            


    ##Tableflip response (with embed)
    @commands.command(name="table",
                      help="Use this command to display a random tableflip.",
                      brief="A command for a random tableflip.",
                      description="Use this command to display a random tableflip.")
    async def _table(self, ctx):
        
        responses = ['(ノ ﾟДﾟ)ノ　＝＝＝＝　┻━━┻',
                    '(/#-_-)/~┻┻〃',
                    '(ノ#-_-)ノ ミ　┴┴',
                    '(╯°□°）╯︵ ┻━┻',
                    '(ノಠ益ಠ)ノ彡┻━┻',
                    'ʕノ•ᴥ•ʔノ ︵ ┻━┻',
                    '(/¯◡ ‿ ◡)/¯ ~ ┻━┻',
                    '(ノ-_-)ノ ~┻━┻',
                    '(ﾉ；；)ﾉ~┻━┻',
                    '(ﾉ-_-)ﾉ ~┻━┻ ☆`',
                    '(ノ-_-)ノ・・・~~┻━┻',
                    'ノ￣□￣)ノ ~┻━┻',
                    '(ﾉꐦ ⊙曲ఠ)ﾉ彡┻━┻',
                    '(ﾉ｀□´)ﾉ⌒┻━┻',
                    '(ﾉꐦ ๑´Д`๑)ﾉ彡┻━┻',
                    '┻━┻ミ＼（≧ロ≦＼）',
                    '(ﾉ￣□￣)ﾉ ~┻━┻',
                    '（ノ♯｀△´）ノ~’┻━┻',
                    '（ノT＿T)ノ ＾┻━┻',
                    '(┛ಠДಠ)┛彡┻━┻',
                    '(ノ°▽°)ノ︵┻━┻',
                    '(ﾉ*’ω’*)ﾉ彡┻━┻',
                    '‎(ﾉಥ益ಥ）ﾉ ┻━┻',
                    '(._.) ~ ︵ ┻━┻',
                    '(╯’□’)╯︵ ┻━┻',
                    '┗[© ♒ ©]┛ ︵ ┻━┻',
                    '┻━┻ ︵ ლ(⌒-⌒ლ)',
                    '(ﾉ＾◡＾)ﾉ︵ ┻━┻',
                    'ヽ༼ ツ ༽ﾉ ︵┻━┻',
                    '(╯ ͝° ͜ʖ͡°)╯︵ ┻━┻',
                    '(┛◉Д◉)┛彡┻━┻',
                    '(ﾉ≧∇≦)ﾉ ﾐ ┸━┸',
                    '┻━┻ミ＼(≧ﾛ≦＼)',
                    '(ノ｀´)ノ ~┻━┻ ～',
                    '(ﾉ▼д▼)ﾉ ~┻━┻ ☆`',
                    '┻━┻ ︵ ლ(ಠ益ಠლ)',
                    '(┛❍ᴥ❍)┛彡┻━┻',
                    '(ノ｀Д´)ノ~┻━┻',
                    '┻━┻ ヘ╰( •̀ε•́ ╰)',
                    '(╯ ･ ᗜ ･ )╯︵ ┻━┻',
                    '!!!!|┛*｀Д´|┛・・~~┻━┻　┳━┳',
                    '(ﾉ≧∇≦)ﾉ ﾐ ┸┸',
                    '(ﾉ｀⌒´)ﾉ ┫：・’.：：・┻┻：・’.：：・',
                    '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻',
                    '(ノÒ益Ó)ノ彡▔▔▏',
                    'ミ(ノ￣^￣)ノ!≡≡≡≡≡━┳━☆()￣□￣)/',
                    '(۶ૈ ۜ ᵒ̌▱๋ᵒ̌ )۶ૈ=͟͟͞͞ ⌨',]
        Title = ((f'{random.choice(responses)}'))
        myembed = discord.Embed(title=Title)
        await ctx.send(embed=myembed) 



#Defines class as cog
def setup(bot):
    bot.add_cog(Fun(bot))