import discord, os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")
    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
client = MyClient()
client.run(TOKEN)