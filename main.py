#!/usr/bin/env python3

import os
import sys
import time
import traceback
import discord
from discord.ext import commands
import methods
from bot import Bot
from constants import *


bot = Bot(prefix)  # noqa: F405


@bot.event
async def on_connect():
  bot.print("Connected to Discord...")
  await bot.wait_until_ready()

  try:
    status = discord.Game(game)  # noqa: F405
    await bot.change_presence(status=discord.Status.online, activity=status)
  except Exception:
    pass

  bot.print(f"Logged in as {bot.user}")
  bot.print(f"Command prefix: '{bot.command_prefix}'")


if __name__ == "__main__":
  for ext in ['cogs.owner', 'cogs.utils']:
    try:
      bot.load_extension(ext)
    except Exception as e:
      bot.print(f"Failed to load extension {ext}", file=sys.stderr)
      traceback.print_exc()

  methods.start_logger(logging_level)  # noqa: F405
  bot(token, bot=True)  # noqa: F405
