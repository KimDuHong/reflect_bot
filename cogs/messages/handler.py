from discord.ext import commands
import discord

class MessageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # 받은 메시지의 author 가 bot 인 경우 return
        if message.author.bot:
            print("bot : " + message.content)
            return None

        channel = message.channel
        msg = message.content
        print("user : " + msg)
        await channel.send("TEST")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.name == "zghik5":
            embed = discord.Embed(title=message.content, color=0x00AAAA)
            embed.set_author(name="Deleted Message", icon_url=message.author.avatar.url)
            await message.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.name == "zghik5":
            embed = discord.Embed(title=f"{before.content} -> {after.content}", color=0x00AAAA)
            embed.set_author(name="Edited Message", icon_url=before.author.avatar.url)
            await before.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MessageCommands(bot))
