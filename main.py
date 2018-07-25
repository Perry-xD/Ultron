#!/usr/bin/env python3

import re
import os
import sys
import time
import asyncio
import traceback
import discord
from discord.ext import commands
import constants as C
import methods
from bot import Bot


bot = Bot(methods.choose_prefix(C.prefix, C.prefixes))


@bot.event
async def on_connect():
  bot.print("Connected to Discord...")
  await bot.wait_until_ready()

  try:
    game = discord.Game(C.game)
    await bot.change_presence(status=discord.Status.online, activity=game)
  except Exception:
    pass

  bot.print(f"Logged in as {bot.user}")
  bot.print(f"Command prefix: '{bot.command_prefix}'")


@bot.event
async def on_command_error(ctx, e):
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

  bot.print(e)


if __name__ == "__main__":
  for ext in ['cogs.owner', 'cogs.utils']:
    try:
      bot.load_extension(ext)
    except Exception as e:
      bot.print(f"Failed to load extension {ext}", file=sys.stderr)
      traceback.print_exc()

  bot(C.token, bot=True)
