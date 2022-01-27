import discord 
from discord.ext import commands
import random 

TOKEN  = "OTM0Mzc1MjI3NjU0MzAzNzc1.YevKvg.oOGBaDGC4lIjBfWjozDPt4xjquQ"
PREFIX = '!'
bot    = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    print('Logged on as', bot.user)
    channel = bot.get_channel(930832207998779544)
    await channel.send("Gue onlen nich")

@bot.command() 
async def hello(ctx):
    if ctx.message.author == bot.user: return
    embedVar = discord.Embed(title="Title", description="Desc", color=0x336EFF)
    embedVar.add_field(name="About Me.", value="My name is Teuku Reynaldi Putra Irwansyah, you can call me Rey,Ku, and im 21 years old right now.", inline=False)
    embedVar.add_field(name="Favourie Food", value="Any of sweety food and drinks, hot spicy food, much more.", inline=False)
    await ctx.send(embed=embedVar)

bot.run('OTM0Mzc1MjI3NjU0MzAzNzc1.YevKvg.oOGBaDGC4lIjBfWjozDPt4xjquQ')