import os
import discord
import discord
import pymongo
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv('MONGO_URL')
cluster = MongoClient(MONGO_URL)
db = cluster["UserData"]
collection = db["UserData"]
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('DISCORD_CHANNEL'))  # Assuming the channel ID is an integer

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        # Get the channel by ID
        channel = self.get_channel(CHANNEL)

        # Check if the channel is valid
        if channel is not None:
            # Open the file for writing with UTF-8 encoding
            with open(r"C:\Users\cyrus\OneDrive\Desktop\discord-bot\testFileWrite.txt", "a", encoding="utf-8") as f:
                # Fetch message history
                async for message in channel.history(limit=None):
                    f.write(f"Message from {message.author}: {message.content}\n")
                    post = {"User ID": self.user.id, "Username": message.author.name, "Message": message.content} 
                    collection.insert_one(post)
                    for reaction in message.reactions:
                        async for user in reaction.users():
                            f.write(f"Reaction {reaction.emoji} added by {user}\n")
                            post = {"Username": self.user.name, "Reaction": reaction.emoji}
                            collection.insert_one(post)
        else:
            print("Channel not found or bot doesn't have access.")

    async def on_message(self, message):
        if message.channel.id == CHANNEL:
            post = {"User ID": message.author.id, "Username": message.author.name, "Message": message.content} 
            collection.insert_one(post)
        if message.channel.id == CHANNEL:
            # Open the file for appending with UTF-8 encoding
            with open(r"C:\Users\cyrus\OneDrive\Desktop\discord-bot\testFileWrite.txt", "a", encoding="utf-8") as f:
                # Write new message author and content to file
                f.write(f"Message from {message.author}: {message.content}\n")
                # post = {"User ID": self.user.id, "Username": message.author.name, "Discriminator": self.user.discriminator, "Messager": message.content} 
                # collection.insert_one(post)

    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id == CHANNEL:
            post = {"User ID": user.id, "Username": user.name, "Reaction": reaction.emoji}
            collection.insert_one(post)
        if reaction.message.channel.id == CHANNEL:
            # Open the file for appending with UTF-8 encoding
            with open(r"C:\Users\cyrus\OneDrive\Desktop\discord-bot\testFileWrite.txt", "a", encoding="utf-8") as f:
                # Write new reaction added by user to file
                f.write(f"Reaction {reaction.emoji} added by {user}\n")
                # post = {"Username": self.user.name, "Reaction": reaction.emoji}
                # collection.insert_one(post)

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = MyClient(intents=intents)
client.run(TOKEN)
