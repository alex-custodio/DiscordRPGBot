import discord, os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    async def on_message(self, message):
        if message.content.startswith('/Jogar'):
            await message.channel.send('Bem vindo a este rpg interativo\n/Curiosidades\nEscolher personagem')
        if message.content.startswith('/Curiosidades'):
            await message.channel.send('Você sabia que a língua de uma baleia-azul pode pesar até 3,6 toneladas? Não tem muito a ver com RPG, mas sei lá KSAKASKAK')
        elif message.content.startswith('/Escolher personagem'):
            await message.channel.send('Programador ainda vai trabalhar nisso! Eu prometo')
client = MyClient()
client.run(TOKEN)