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
