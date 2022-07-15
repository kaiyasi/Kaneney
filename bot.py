# 系統預設設定
import datetime
import discord
from discord.ext import commands
import json 
import os
from datetime import datetime as dt
client = discord.Client()

with open('setup.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)




#機器人上線
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(),help_command=None)
@bot.event

async def on_ready():

    #狀態顯示系統
    state = ("==================================\n"
    "\n"
    "   機組狀態 : 調度運行中..." + "\n"
    "   登錄系統端: " + str(bot.user) +"\n"
    "   當前時間: " + dt.now().strftime("%Y/%m/%d %H:%M:%S")+"\n"
    "\n"
    "==================================")
    print(state)
    channel = bot.get_channel(int(jdata['data']))
    embed=discord.Embed(title="瓦羅伊備援系統", description="狀態報告", color=0x70cdf5,timestamp=datetime.datetime.utcnow())
    embed.set_author(name="凱恩尼開發團隊")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/983638915204399134/984433555004350484/Picsart_22-06-05_07-09-12-942.jpg")
    embed.add_field(name="✠ 運作狀態", value=" • 備援運行中... ", inline=True)
    embed.add_field(name="☬ 運作版本", value=" • " + jdata['version'], inline=False)
        #embed.add_field(name="━  移除", value="•  ", inline=False)
    embed.set_footer(text=" 🛠️ 團隊私人備援系統 🛠️ ")
    await channel.send(embed=embed)   


    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    
    status_w = discord.Status.online

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.watching, name="設置中...")

    await bot.change_presence(status= status_w, activity=activity_w)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['formal']) 