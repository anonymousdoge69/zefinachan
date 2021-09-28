#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telethon import TelegramClient, events
import os


TOKEN = os.getenv("TOKEN")
API_KEY, API_HASH = os.getenv("API_KEY"), os.getenv("API_HASH")

bot = TelegramClient(None, API_KEY, API_HASH

bot.start(bot_token=TOKEN)

@bot.on(events.NewMessage(pattern="^[!/](http|socks4|socks5)$", func=lambda e: e.is_private or e.is_group))
async def get_proxies(e):
 mode = e.text[1:]
 r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol={}&timeout=10000&country=all&ssl=all&anonymity=all".format(mode))
 with io.BytesIO(r.content.encode()) as file:
      file.name = "{}_proxies.txt".format(mode)
      await e.reply(file=file)
