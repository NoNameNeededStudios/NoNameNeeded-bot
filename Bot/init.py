#!THIS IS SO THAT THE FILES/COGS CAN RUN

































#!THIS IS SO THAT THE FILES/COGS CAN RUN

































import random
import json
import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from discord.utils import get
import discord
from discord.ext import commands
import datetime 
from itertools import cycle
import os

import asyncio
import datetime
from discord.ext.commands import when_mentioned_or
import asyncio
import functools
import itertools
import math
import random
from random import choice
from discord.voice_client import VoiceClient
import youtube_dl
from async_timeout import timeout
from discord.ext.commands import Cooldown, CommandOnCooldown, MissingRequiredArgument, CommandInvokeError, MissingAnyRole,CommandNotFound, MemberNotFound
from PIL import Image
from io import BytesIO
from discord.utils import get
from youtubesearchpython import SearchVideos
import wolframalpha
from asyncio import sleep
import requests
from gtts import gTTS
from discord.ext.commands import Bot



client = Bot(command_prefix= ["n!", "N!", "N?", "n?"])  

em_colors = [discord.Colour.red, discord.Colour.blue ,  discord.Colour.green, discord.Colour.orange, discord.Colour.gold, discord.Colour.dark_orange, discord.Colour.dark_blue]






client.remove_command("help")  




@client.command()
async def help(ctx):
    print(f"helped {ctx.author}")


@client.event
async def on_ready(ctx):
   channel = client.get_channel(797161993748217876)
   await channel.send("Bot is Online | <@730505256953446422>")



   

#!_--------_Load Cogs_--------_!#

Invite = "https://discord.com/api/oauth2/authorize?client_id=786164164690706462&permissions=2147483639&scope=bot"



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

     
    

client.run("hahah u think token here? no fuk ur self")



