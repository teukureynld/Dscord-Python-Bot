import discord


Client = discord.Client()

async def mention(ctx, user : "935879312194801744"):
    await ctx.send(user.mention)

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return

    if message.content.startswith('hallo'):
        await message.channel.send('Hi~')
        user_id = '<@935879312194801744'
        await message.channel.send(f"<@{user_id}> is the best")

    
Client.run("Your_Token_Bot")

        


