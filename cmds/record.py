
import datetime
from email import message
import re

from core.classes import Cog_extension
from discord.ext import commands
import discord
from core.classes import Cog_extension
import json
with open('setup.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)






class Record(Cog_extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        record = self.bot.get_channel(int(jdata['record']))
        embed=discord.Embed(title="紀錄系統", description="紀錄內容 : 成員變動", color=0xb1f881, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="• 成員狀態", value="✚ 加入", inline=True)
        embed.add_field(name="• 成員ID", value=f'{member.mention}', inline=True)
        embed.set_footer(text="凱恩尼紀錄系統 ")
        await record.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self,member):
        record = self.bot.get_channel(int(jdata['record']))
        embed=discord.Embed(title="紀錄系統", description="紀錄內容 : 成員變動", color=0xf56666, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="• 成員狀態", value="━ 離開", inline=True)
        embed.add_field(name="• 成員ID", value=f'{member.mention}', inline=True)
        embed.set_footer(text="凱恩尼紀錄系統 ")
        await record.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        record = self.bot.get_channel(int(jdata['record']))
        if len(msg.content) == 0:
            msg.content = " 此訊息為崁入訊息 無法進行記錄 "
        else:
            pass

        embed=discord.Embed(title="紀錄系統", description="紀錄內容 : 訊息刪除", color=0xf882bb, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="• 訊息內容", value=f"```➢ {msg.content} ```", inline=False)
        embed.add_field(name="• 成員ID", value=f'{msg.author.mention}', inline=False)
        embed.set_footer(text="凱恩尼紀錄系統 ")
        await record.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.content != after.content:
            record = self.bot.get_channel(int(jdata['record']))
            embed=discord.Embed(title="紀錄系統", description="紀錄內容 : 訊息編輯", color=0xf6f882, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="• 原訊息", value=f"```➢ {before.content} ```", inline=False)
            embed.add_field(name="• 新訊息", value=f"```➢ {after.content} ```", inline=False)
            embed.add_field(name="• 訊息者ID", value=f'{before.author.mention}', inline=True)
            embed.set_footer(text="凱恩尼紀錄系統 ")
            await record.send(embed=embed)
            await record.send({after.jump_url})


def setup(bot):
    bot.add_cog(Record(bot))