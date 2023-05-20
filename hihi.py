import discord
from discord.ext.commands import Bot
import os
import time
import random

intents=discord.Intents.default()
bot = Bot(command_prefix='~', intents=intents)

Papering = False
PaperNum = 0

TheNum = 0

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

#@bot.event()
async def on_typing(channel, user, when):
    await channel.send(str(user)+"야 뭐적냐")
    return

@bot.command()
async def 안녕(ctx):
    await ctx.send('네, 주인님')

@bot.command()
async def 도배해줘(ctx, text,number):
    if Papering == True:
        await ctx.send(text+"를 "+number+" 번 도배하겠습니다")
        await ctx.send("도배해줘")

@bot.command()
async def 도배그만(ctx):
    await ctx.send("그만 도배하겠습니다")
    Papering = False

@bot.command()
async def 메뉴추천해줘 (ctx, M1,M2,M3,M4,M5):
    TheNum = random.randrange(1,6)
    if TheNum==1:
        await ctx.send(M1+"을(를) 추천합니다")
    elif TheNum==2:
        await ctx.send(M2+"을(를) 추천합니다")
    elif TheNum==3:
        await ctx.send(M3+"을(를) 추천합니다")
    elif TheNum==4:
        await ctx.send(M4+"을(를) 추천합니다")
    elif TheNum==5:
        await ctx.send(M5+"을(를) 추천합니다")
@메뉴추천해줘.error
async def 메뉴추천해줘_error(ctx, error):
    await ctx.send("메뉴를 5개 입력해 주세요")

bot.run("MTEwOTQ1NjAzMDcwODAyMzM0Ng.Gc8I64.LVj5CFF0E4jY4HCYwDcLDI1vc3ALavvkeutnJM")
