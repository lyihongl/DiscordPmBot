import discord
import re
import sqlite3
from contextlib import closing
from discord.ext import commands


conn = sqlite3.connect('dpb-dev')
bot = commands.Bot(command_prefix='!')

# architecture
# project -> issue -> branch


@bot.command(name='gourd')
async def gourd(ctx, *arg):
    print(arg)
    await ctx.send(arg)

def parse_message(message):
    pass

bot.run('ODA0MjE2ODc5OTUzODcwODg4.YBJHVQ.p4EnYKdBcGB4gBMqc6Jb7P60-y0')
