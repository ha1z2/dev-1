import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await message.channel.send('ㅎㅇ')


client.run("NzA5MDI4ODg0OTIxODQzNzIy.Xrf9sQ.vgnHKZDgFWe-8SUFOnYf46IeQ-M")