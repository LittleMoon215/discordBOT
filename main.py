import asyncio
import random
from typing import List

import requests

import lists
import discord
from discord import AllowedMentions, User, Member, Intents, TextChannel, ChannelType
from discord.ext import commands
from discord.ext.commands import Context

from config import settings

intents: Intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
_annoy = False

@bot.command()
async def bully(ctx: Context, tag):
    members: List[Member] = ctx.guild.members
    user: User = discord.utils.get(members, discriminator=tag)
    if user:
        await ctx.send(f'{user.mention} {random.choice(lists.bully)}', allowed_mentions=AllowedMentions(users=True))
    else:
        await ctx.send('User not found')


@bot.command()
async def anime(ctx: Context):
    response = requests.get("https://some-random-api.ml/animu/wink").json()
    embed = discord.Embed(color=0xff9900, title='Random anime winking')
    embed.set_image(url=response['link'])
    await ctx.send(embed=embed)


@bot.command()
async def meme(ctx: Context):
    response = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=0xff9900, title='Random meme')
    embed.set_image(url=response['image'])
    await ctx.send(embed=embed)


@bot.command()
async def annoy(ctx: Context):
    _annoy = True
    channels = [channel for channel in ctx.guild.channels if channel.type == ChannelType.voice]
    while _annoy:
        for channel in channels:
            if channel.
        await asyncio.sleep(5)
bot.run(settings['token'])
