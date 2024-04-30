import os
import discord
import pymongo
import asyncio
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
            try:
                post = {"User ID": message.author.id, "Username": message.author.name, "Message": message.content} 
                collection.insert_one(post)
                print("Message inserted into the database successfully.")
            except Exception as e:
                print(f"Error inserting message into the database: {e}")

    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id == CHANNEL:
            try:
                post = {"User ID": user.id, "Username": user.name, "Reaction": str(reaction.emoji)} 
                collection.insert_one(post)
                print("Reaction inserted into the database successfully.")
            except Exception as e:
                print(f"Error inserting reaction into the database: {e}")

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = MyClient(intents=intents)

async def main():
    try:
        await client.start(TOKEN)
    except Exception as e:
        print(f"An error occurred while starting the client: {e}")

asyncio.run(main())
