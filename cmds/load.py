
import datetime
from core.classes import Cog_extension
import discord
from discord.ext import commands
from core.classes import Cog_extension
import json
with open('setup.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)





class Load(Cog_extension):

    #載入模組
    @commands.command()
    async def load(self,ctx,extension):
        try:
            self.bot.load_extension(f'cmds.{extension}')
        except:
            await ctx.send("☢ 錯誤 : 發生意外錯誤 請重新載入 或通知製作人 ☢")
        else:
            await ctx.send(f'模組庫 【{extension}】 已載入完成')
            with open('setup.json', 'r', encoding='utf-8') as f:
                p = json.load(f)
                p["loaded"].append(str(extension))
            with open('setup.json', 'w', encoding='utf-8') as f:
                json.dump(p, f,indent=4, ensure_ascii=False)



    # 重新載入模組
    @commands.command()
    async def reload(self,ctx,extension):
        self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'模組庫 【{extension}】 已重載完成')


    #卸載模組
    @commands.command()
    async def unload(self,ctx,extension):
        try:
            self.bot.unload_extension(f'cmds.{extension}')
        except:
            await ctx.send("☢ 錯誤 : 發生意外錯誤 請重新卸載 ☢")
        else:
            await ctx.send(f'模組庫 【{extension}】 已卸載完成')
            with open('setup.json', 'r', encoding='utf-8') as f:
                p = json.load(f)
                p["loaded"].remove(str(extension))
            with open('setup.json', 'w', encoding='utf-8') as f:
                json.dump(p, f,indent=4, ensure_ascii=False)


    #模組清單
    @commands.command()
    async def loadlist(self,ctx):
        enabled = []
        disabled = []
        with open('setup.json', 'r', encoding='utf-8') as f:
            p = json.load(f)
            for i in p["extensions"]:
                if i in p["loaded"]:
                    enabled.append(i)
                else:
                    disabled.append(i)
            if len(disabled) == 0 :
                disabled.append("全數模組皆已上線服務")
            enabled = ", ".join(enabled)
            disabled = ", ".join(disabled)
            embed=discord.Embed(title="模組狀態", color=0x57fb41,timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/983638915204399134/984433555004350484/Picsart_22-06-05_07-09-12-942.jpg")
            embed.add_field(name="✚ 載入模組", value="•" + f"【{enabled}】", inline=False)
            embed.add_field(name="━ 卸載模組", value="•" + f"【{disabled}】", inline=False)
            embed.set_footer(text="凱恩尼模組系統")
            await ctx.send(embed=embed)
 

    



def setup(bot):
    bot.add_cog(Load(bot))
        