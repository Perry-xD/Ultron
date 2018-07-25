#!/usr/bin/env python3

import json
from os import environ

token = environ.get("TOKEN")
owner = environ.get("OWNER")
prefix = environ.get("PREFIX")

game = environ.get("GAME_STATUS")
