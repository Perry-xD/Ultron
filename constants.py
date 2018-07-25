#!/usr/bin/env python3

import json
from os import environ

token = os.environ.get("TOKEN")
owner = os.environ.get("OWNER")
prefix = os.environ.get("PREFIX")

game = os.environ.get("GAME_STATUS")