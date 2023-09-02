import discord
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi")
    elif message.content.startswith('bye'):
        await message.channel.send(":thumbsup:")
    else:
        await message.channel.send(message.content)

client.run("MTE0MjQ3MTQ0OTE2OTM3NTI1Mw.GnI9ev.eodjWnwtGPLnLBMrdaPYPRhKXL5BSDTiNdLt9g")

gen_pass(10)


