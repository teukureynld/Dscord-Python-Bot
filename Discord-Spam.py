import discord

Client = discord.Client()

keywords = ["hello","who is me?"]

@Client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(25):
                await message.channel.send('Hallo my Owner!',)
     

Client.run('OTM0Mzc1MjI3NjU0MzAzNzc1.YevKvg.f37YJ-VNvzd1gKNPW6au8D9T2oo')

