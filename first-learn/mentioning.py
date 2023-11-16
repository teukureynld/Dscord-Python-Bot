import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='&', intents=intents)  # renamed bot because you're using an instance of Bot



@bot.command()  # pass_context is not necesary since more than few versions back
async def test(ctx, user_:  # renamed id to user_id to make it more readable
  user = bot.get_user(user_)
  print(user)

TOKEN = ("Your_Token_Bot")
bot.run("Your_Token_Bot")