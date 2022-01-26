import discord
import requests
import json
import random
from korean_romanizer.romanizer import Romanizer

client = discord.Client()
TOKEN = ''

def romanize_this(hankookmal):
    r = Romanizer(hankookmal)
    return(r.romanize())
  
@client.event
async def on_ready():
    print('we have logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
 if msg.startswith('^romanize'):
        r = romanize_this(message.content[9:])
        await message.channel.send(r)

 client.run(TOKEN)

