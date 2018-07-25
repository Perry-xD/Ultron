#!/usr/bin/env python3

import time
import discord
from discord.ext import commands


class OwnerCog:
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.is_owner()
  async def restart(self, ctx):
    await self.bot.logout()
    self.bot.print("Logged out. Shutting down...")
    time.sleep(0.5)
    exit(0)


  @commands.command()
  @commands.is_owner()
  async def shutdown(self, ctx):
    await self.bot.logout()
    self.bot.print("Logged out. Shutting down...")
    time.sleep(0.5)
    exit(1)


def setup(bot):
  bot.add_cog(OwnerCog(bot))
