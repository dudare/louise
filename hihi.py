import discord
from discord.ext.commands import Bot

intents=discord.Intents.default()
bot = Bot(command_prefix='~', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

#@bot.event()
#async def on_typing(channel, user, when):
 #   await channel.send(str(user)+"야 뭐적냐")
  #  return

@bot.command()
async def 안녕(ctx):
    await ctx.send('오하요오~')

@bot.command()
async def 도배(ctx, text,number):
     for i in range(int(number)):
         await ctx.send(text)

bot.run('ODkxNjgxNDMzODY3OTIzNDg2.YVB5DA.y4itpNweBwqKUAl5-q2TgPXU3IY')
