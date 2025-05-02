import discord
from bot_logic import gen_pass

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
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$bye'):
        await message.channel.send("😭👋")

    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    
    elif message.content.startswith('$joke1'):
        await message.channel.send("Why did the scarecrow win an award? Because he was outstanding in his field! 🌾😆")

    elif message.content.startswith('$joke2'):
        await message.channel.send("Why can't your nose be 12 inches long? Because then it would be a foot! 👃➡️🦶😂")

    elif message.content.startswith('!mejor_plastico'):
        await message.channel.send("El polipropileno:" \
        "El polipropileno (PP) se considera un plástico menos contaminante debido a su composición, propiedades y potencial de reciclaje. El PP está compuesto principalmente por carbono e hidrógeno, elementos naturales y no tóxicos. Además, es un material relativamente ligero y resistente, lo que reduce la necesidad de grandes cantidades para fabricar productos, disminuyendo así el desperdicio y la huella de carbono. ")

    elif message.content.startswith('!top_plasticos'):
        await message.channel.send("Los plasticos menos contaminantes son los siguientes                                                                        " \
        "3.polietileno tereftalato (PET)                                    " \
        "2.el polietileno de alta densidad (HDPE)                      " \
        "1.el polipropileno (PP)                                             ")



client.run("*youre discord token")
