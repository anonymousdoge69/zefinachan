#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telethon import TelegramClient, events, Button
import os, io
import requests, logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
  )

TOKEN = os.getenv("TOKEN")
API_KEY, API_HASH = os.getenv("API_KEY"), os.getenv("API_HASH")

bot = TelegramClient(None, API_KEY, API_HASH)

bot.start(bot_token=TOKEN)

@bot.on(events.NewMessage(pattern="^[!/](http|socks4|socks5)$", func=lambda e: e.is_private or e.is_group))
async def get_proxies(e):
 mode = e.text[1:]
 r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol={}&timeout=10000&country=all&ssl=all&anonymity=all".format(mode))
 with io.BytesIO(r.content) as file:
      file.name = "{}_proxies.txt".format(mode)
      await e.respond(file=file)

@bot.on(events.NewMessage(pattern="^[/!]start$", func=lambda e: e.is_private))
async def _start(e):
 await e.respond("""
✨ ZefinaProxy~ ✨

✅For Http(S) click /http
✅For Socks5 click /socks5
✅For Socks4 click /socks4

By using our service you agree to our terms of use!
• The Bot Downloads proxies from proxyscrape to make your work easy
• For Free Stuff Join: @piro_giveaways (Happy Cracking :)
""", buttons=[Button.text("HTTP", resize=True), Button.text("SOCKS4", resize=True), Button.text("SOCKS5", resize=True)])

@bot.on(events.NewMessage(pattern="^HTTP", func=lambda e: e.is_private))
async def http__(e):
 r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
 with io.BytesIO(r.content) as file:
      file.name = "http_proxies.txt"
      await e.respond(file=file)

@bot.on(events.NewMessage(pattern="^SOCKS4", func=lambda e: e.is_private))
async def socks4__(e):
 r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
 with io.BytesIO(r.content) as file:
      file.name = "socks4_proxies.txt"
      await e.respond(file=file)

@bot.on(events.NewMessage(pattern="^SOCKS5", func=lambda e: e.is_private))
async def socks5__(e):
 r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
 with io.BytesIO(r.content) as file:
      file.name = "socks5_proxies.txt"
      await e.respond(file=file)

bot.run_until_disconnected()
