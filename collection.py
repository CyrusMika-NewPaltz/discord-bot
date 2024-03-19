# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
f = open(r"C:\Users\cyrus\testFileWrite.txt", "w")   # 'r' for reading and 'w' for writing
members = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
                # Get the channel by ID
        channel = client.get_channel(1214586809774907425)
        
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
        channel = client.get_channel(1214586809774907425)
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
client.run('MTIxNDQ3MTczOTU3MzAxNDU3OQ.GEo5YS.N737hTLYUGIS6P4vMcTHlzWVBmehTcr0geeex0')


