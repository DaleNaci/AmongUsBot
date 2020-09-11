import asyncio

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
from discord.utils import find
from discord import Color, Embed


class Toggle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.isMuted = False
        self.vc_id = 510115905041203204

    @commands.command()
    async def toggle(self, ctx):
        self.isMuted = not self.isMuted

        channel = self.bot.get_channel(self.vc_id)
        members = channel.members

        for m in members:
            await m.edit(mute=not self.isMuted)


        if not self.isMuted:
            title = "Muting Everyone."
            color = Color.red()
        else:
            title = "Unmuting Everyone."
            color = Color.green()

        embed = Embed(
                    title=title,
                    color=color
                )

        await ctx.send(embed=embed)


    @commands.command()
    async def t(self, ctx):
        await self.toggle(ctx)


def setup(bot):
    bot.add_cog(Toggle(bot))
