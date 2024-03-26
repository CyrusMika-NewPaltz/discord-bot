import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('DISCORD_CHANNEL'))  # Assuming the channel ID is an integer

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        # Get the channel by ID
        channel = self.get_channel(CHANNEL)

        # Check if the channel is valid
        if channel is not None:
            # Open the file for writing
            with open(r"C:\Users\cyrus\OneDrive\Desktop\discord-bot\testFileWrite.txt", "a") as f:
                # Fetch message history
                async for msg in channel.history(limit=200):
                    # Write message author and content to file
                    f.write(f"{msg.author}: {msg.content}\n")
        else:
            print("Channel not found or bot doesn't have access.")

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.author.id)
        if message.channel.id == CHANNEL:
            # Open the file for appending
            with open(r"C:\Users\cyrus\OneDrive\Desktop\discord-bot\testFileWrite.txt", "a") as f:
                # Write new message author and content to file
                f.write(f"{message.author}: {message.content}\n")
        f.close()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
