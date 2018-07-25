#!/usr/bin/env python3

import logging
import discord
from discord.ext import commands


def choose_prefix(default, *prefixes):
  def prefix(bot, message):
    if not message.guild:
      return default

    return commands.when_mentioned_or(*prefixes)(bot, message)
  return prefix


def start_logger(level):
  logger = logging.getLogger('discord')
  logger.setLevel(eval(f"logging.{level}"))

  fmt = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")

  handler = logging.FileHandler("/app/cache/discord.log", "a+", "utf-8")
  handler.setFormatter(fmt)

  logger.addHandler(handler)
