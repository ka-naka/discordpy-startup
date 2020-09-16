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

@client.event
async def on_message(message):
    if message.author.bot:  # ボットのメッセージをハネる
        return
    if message.content == "!眠たい":
       # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "!投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたは右利きですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "!おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ")

    elif message.content == "help":
        # チャンネルへメッセージを送信
         await message.channel.send("これはイベントつぶやきBOTです。今日と明日の定時イベントをリストアップします")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == ("!event" or "!events" or "!イベント" or "！イベント")
        Events_array=["勢力の拡大", "部隊訓練", "研究", "Dragonの拡大", "モンスター討伐", "勢力の拡大", "資源の収集", "部隊訓練", "モンスター討伐", "建設", "部隊訓練", "Dragonの拡大", "モンスター討伐"]

        dt_s =  datetime.datetime(2020, 1, 1, 0, 0,0)
        dt_n =  datetime.datetime(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day,0,0,0)

        h=0
        ev = (((dt_n-dt_s).days)*24 % 13)
        while h<48:
            await message.channel.send("今日と明日のイベント一覧")
            await message.channel.send(dt_n,Events_array[ev])
            ev=ev+1
            h=h+1
            dt_n = dt_n+datetime.timedelta(hours=1)
            if ev==13:
             ev=0
            if h==24:
            await message.channel.send("-----")
    
bot.run(token)
