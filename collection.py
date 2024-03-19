# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL')

f = open(r"C:\Users\cyrus\testFileWrite.txt", "w")   # 'r' for reading and 'w' for writing
members = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
                # Get the channel by ID
        channel = client.get_channel(CHANNEL)
        
        # Check if the channel is valid
        if channel is not None:
            # Fetch message history
            messages = []
            async for msg in channel.history(limit=200):
                messages.append(msg)
            
            for msg in messages:
                print(msg.content)
                print(msg.author)
                if msg.author not in members:
                    members.append(msg.author)
                f.write(str(msg.author)+" : "+str(msg.content))    # Write inside file
                f.write(" \n")
            for mem in members:
                print(mem)
        else:
            print("Channel not found or bot doesn't have access.")

    async def on_message(self, message):
        channel = client.get_channel(CHANNEL)
        print(f'Message from {message.author}: {message.content}')
        print(message.author.id)
        # Check if the channel is valid
        if channel is not None:
            # Fetch message history
            messages = []
            async for msg in channel.history(limit=200):
                messages.append(msg)
            
            for msg in messages:
                print(msg.content)
                print(msg.author)
                if msg.author not in members:
                    members.append(msg.author)
                f.write(str(msg.author)+" : "+str(msg.content))    # Write inside file
                f.write(" \n")
            for mem in members:
                print(mem)
            f.close()

        


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)


