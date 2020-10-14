import discord #inportuje discord.py

client = discord.Client()

@client.event
async def on_ready():
    print('Zalogowano jako {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Witam'):
        await message.channel.send('Cześć {0.author.mention}!'.format(message))


client.run('NzY1OTE5ODU1MjQ1MDAwNzI2.X4b0cw.mqO2ZXLPAEj7yF-lB10rovWy-vQ')
