# 指令系統 
# 系統預設設定
import datetime
import discord
from discord.ext import commands
from core.classes import Cog_extension
import json
import time
client = discord.Client()
with open('setup.json','r',encoding='utf8') as jfile: 
    jdata = json.load(jfile)


class Inout(Cog_extension):


    @commands.Cog.listener()
    async def on_member_join(self,member): 
        welcome = self.bot.get_channel(int(jdata['welcome']))
        rule = self.bot.get_channel(int(jdata['rule']))

        embed=discord.Embed(title="成員變動", description="狀態 : 加入", color=0x84f882,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="🛡️ 成員", value=f'{member.mention}', inline=True)
        embed.add_field(name="📀 加入日期", value=time.strftime('%Y-%m-%d'), inline=True)
        embed.add_field(name="📜 歡迎加入", value=f'歡迎加入 〚 {member.guild.name} 〛 \n請先至 {rule.mention} 閱讀規章 並領取身分組 \n感謝您的加入', inline=False)
        embed.set_footer(text="凱恩尼人員系統")
        await welcome.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self,member): 
        leave = self.bot.get_channel(int(jdata['leave']))

        embed=discord.Embed(title="成員變動", description="狀態 : 離開", color=0xf88282,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="🛡️ 成員", value=f'{member.mention}', inline=True)
        embed.add_field(name="📀 離開日期", value=time.strftime('%Y-%m-%d'), inline=True)
        embed.add_field(name="📜 希望再度回歸", value=f' {member.mention}  因未知原因離開 {member.guild.name} \n讓我們希望他可以再次回歸  感謝您曾經的加入', inline=False)
        embed.set_footer(text="凱恩尼人員系統")
        await leave.send(embed=embed)


    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'當前ping值: {round(self.bot.latency*1000)} /毫秒')
   

def setup(bot):
    bot.add_cog(Inout(bot))
        