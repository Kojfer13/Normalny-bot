import discord #inportuje discord.py

client = discord.Client()

@client.event
async def on_ready():
    print('Zalogowano jako {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(':everyone'):
        await message.channel.send('@everyone')


client.run('NzY1OTE5ODU1MjQ1MDAwNzI2.X4b0cw.zMYrSf7S1EnUS7ZcS9ybUL-ngJM')