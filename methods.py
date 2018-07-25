#!/usr/bin/env python3

from discord.ext import commands


def choose_prefix(default, *prefixes):
  def prefix(bot, message):
    if not message.guild:
      return default

    return commands.when_mentioned_or(*prefixes)(bot, message)
  return prefix
