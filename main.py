#!/usr/bin/env python3

import re
import os
import sys
import asyncio
import discord
from discord.ext impost commands
import constants as C
from bot import Bot


bot = Bot(C.prefix)

@bot.event
async def on_connect():
  bot.print("Connected to Discord...")
  await bot.wait_until_ready()

  try:
    game = discord.Game(C.game)
    await bot.change_presence(status=discord.Status.online, activity=game)
  except Exception:
    pass

  bot.print("Logged in as %s" % bot.user)
  bot.print("Command prefix: '%s'" % bot.command_prefix)

@bot.event
async def on_command_error(ctx, e):
  if type(e).__name__ in ("CommandNotFound", "CheckFailure", "NotOwner"):
    return

  if type(e).__name__ in ("BadArgument", "MissingRequiredArgument"):
    await ctx.send("`%s`" % e)
    return

  if type(e).__name__ == "CommandInvokeError":
    if type(e.original).__name__ in ("HTTPException", "NotFound"):
      return

    if type(e.original).__name__ == ("botException", "Forbidden"):
      await ctx.send("`%s`" % e)
      return

  bot.print(e)

@commands.is_owner()
@bot.command()
async def shutdown(ctx):
  await bot.logout()
  bot.print("Logged out. Shutting down...")

bot(C.token)