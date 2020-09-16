from discord.ext import commands
import os
import traceback
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()  # 接続に使用するオブジェクト

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def event(ctx):
    Events_array=["勢力の拡大", "部隊訓練", "研究", "Dragonの拡大", "モンスター討伐", "勢力の拡大", "資源の収集", "部隊訓練", "モンスター討伐", "建設", "部隊訓練", "Dragonの拡大", "モンスター討伐"]
    dt_s =  datetime.datetime(2020, 1, 1, 0, 0,0)
    dt_n =  datetime.datetime(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day,0,0,0)
    h=0
    ev = (((dt_n-dt_s).days)*24 % 13)
    while h<48:
        await  ctx.send("今日と明日のイベント一覧")
        await  ctx.send(dt_n,Events_array[ev])
        ev=ev+1
        h=h+1
        dt_n = dt_n+datetime.timedelta(hours=1)
        if ev==13:
         ev=0
        if h==24:
        await  ctx.send("-----")

bot.run(token)
