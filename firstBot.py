import discord >> memuat Library dictionary discord atau memuat program2 yang ada di dc

Client = discord.Client() >> sebagai variable bot

@Client.event

async def on_ready(): 
    print('Sukses login sebagai {0.user}'.format(Client))
    
///Line 7 menyatakan login bot sukses login dari api discord,

@Client.event
async def on_message(message):
    if message.author == Client.user:
        return

    if message.content.startswith('hallo'):
        await message.channel.send('Hi~')
    if message.content.startswith('Who is me?'):
        await message.channel.send('You are my owner!')
    if message.content.startswith('Describe me'):
        await message.channel.send('Your name is Teuku Reynaldi, a fat guy who has a weight of 92 Kgs, a black shorthair!')
    if message.content.startswith('What is favourite food and kind of food did i love?'):
        await message.channel.send('Your favourite food is Crepes and your top of favourite food is a sweetfood')
    if message.content.startswith('Thank you for your fast responses!'):
        await message.channel.send('That is okay, dont mention it, see ya!')


Client.run('///variable token bot\\\')

//////Line 13 - Line 14 adalah sebagai untuk persiapan bot untuk mencetak pesan\\\\

/////Line 15 adalah variable statement if untuk user(pengguna) bot untuk mengirim chat lalu dikirimkan lagi dari bot ke user.
  syntax return adalah Looping yang berfungsi supaya bot tidak error alias tidak mencari pesan yang kosong\\\\\
  
 ////Line 18-27 adalah pesan yang dikirim dari user lalu bot akan membaca lalu mengirimnya lagi.\\\
 
 ////fungsi await.message.channel.send adalah sebagai text timbal balik dari bot\\\\
 
 Client.Run('YOUR TOKEN')
 // Cek pada bagian discord develpoment portal, cek pada bagian reavel token, lalu copas \\\
 
