import discord
from discord import Embed
from discord.ext import commands
import random




class Messages(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    

    ##Tableflip response (with embed)
    @commands.command(name="table",
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
        await ctx.send(embed=myembed) ##(f'> {random.choice(responses)}')





#Defines class as cog
def setup(bot):
    bot.add_cog(Messages(bot))