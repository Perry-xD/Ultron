#!/usr/bin/env python3

import discord
from discord.ext import commands


class UtilsCog:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    await ctx.send("Pong! ({0:d}ms)".format(self.bot.latency * 1000),
                   delete_after=10)

  async def on_message(self, msg):
    await self.bot.process_commands(msg)

    if self.bot.id in [m.id for m in msg.mentions]:
      prefix = self.bot.command_prefix
      mention = msg.author.mention
      await msg.channel.send(f"My current prefix is `{prefix}` {mention}")


def setup(bot):
  bot.add_cog(UtilsCog(bot))
