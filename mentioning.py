import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='&', intents=intents)  # renamed bot because you're using an instance of Bot



@bot.command()  # pass_context is not necesary since more than few versions back
async def test(ctx, user_935879312194801744):  # renamed id to user_id to make it more readable
  user = bot.get_user(user_935879312194801744)
  print(user)

TOKEN = "OTM0Mzc1MjI3NjU0MzAzNzc1.YevKvg.f37YJ-VNvzd1gKNPW6au8D9T2oo"
bot.run('OTM0Mzc1MjI3NjU0MzAzNzc1.YevKvg.f37YJ-VNvzd1gKNPW6au8D9T2oo')