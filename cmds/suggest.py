
import datetime
from webbrowser import get
from core.classes import Cog_extension
import discord
from discord.ext import commands
from core.classes import Cog_extension
import json
with open('setup.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)





class Suggest(Cog_extension):

    @commands.command()
    async def report(self,ctx,re,):
        member = ctx.message.author
        report = self.bot.get_channel(996616863712825444)
        embed=discord.Embed(title="錯誤回報", color=0x57fb41,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/983638915204399134/984433555004350484/Picsart_22-06-05_07-09-12-942.jpg")
        embed.add_field(name="• 回報內容 ", value="➢ " + re , inline=False)
        embed.add_field(name="• 回報者", value=f"➢ {member.mention} ", inline=False)
        embed.add_field(name="• 狀態", value="➢ 已將回報內容傳送至開發團隊 感謝您的回報" , inline=False)

        embed.set_footer(text="凱恩尼回報系統")
        await ctx.send(embed=embed)
        await report.send(embed=embed)

    @commands.command()
    async def editmessage(self,ctx, chann: int, id: int, *, newmsg: str):
        try:
            cha = self.bot.get_channel(chann)
            msg = await cha.fetch_message(id)
        except discord.errors.NotFound:
            await ctx.send(f'查無此`{id}`')
            return
        if msg.author != ctx.guild.me:
            await ctx.send("那個訊息TMD不是我說的")
            return
        owo = await msg.edit(content=newmsg)
        await ctx.send(f'修改完畢[點我傳送AWA]({newmsg.jump_url})')

    @commands.command()
    async def say(self,ctx,thin):
        await ctx.send(thin)

def setup(bot):
    bot.add_cog(Suggest(bot))