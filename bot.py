#!/usr/bin/env python3

from datetime import datetime
import discord
from discord.ext import commands


class Bot(commands.Bot):
  def __call__(self, *args, **kwargs):
    self.print("Running bot now...")
    self.run(*args, **kwargs)

  def print(self, *args, **opts):
    time = datetime.now().strftime("[%T]")
    print(time, *args, **opts)

  async def on_ready(self):
    try:
      app = await self.application_info()

      self.owner = app.owner
      self.id = app.id
    except Exception as e:
      pass

  async def on_command_error(self, ctx, e):
    if type(e).__name__ in ("CommandNotFound", "CheckFailure", "NotOwner"):
      return

    if type(e).__name__ in ("BadArgument", "MissingRequiredArgument"):
      await ctx.send(f"`{e}`")
      return

    if type(e).__name__ == "CommandInvokeError":
      if type(e.original).__name__ in ("HTTPException", "NotFound"):
        return

      if type(e.original).__name__ == ("botException", "Forbidden"):
        await ctx.send(f"`{e}`")
        return

    self.bot.print(e)
