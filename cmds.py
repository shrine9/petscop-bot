import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '//')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='//help'))
    await client.send_message(member, 'Heyyy')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!ping':
        await client.send_message(message.channel,'Pong!')
    if ('spacex') in message.content:
       await client.delete_message(message)
    if ('elon') in message.content:
       await client.delete_message(message)
    if ('musk') in message.content:
       await client.delete_message(message)
    if ('elonmusk') in message.content:
       await client.delete_message(message)
    if ('muskelon') in message.content:
       await client.delete_message(message)
client.run('NDk0MDE5Nzk1ODc3MTAxNTc4.DotbjA.K36HXK3mFHYyi4QrH-d18ow8JYM')
