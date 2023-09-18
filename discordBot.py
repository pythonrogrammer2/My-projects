#invite link: 

# bot token: 

import discord
import os



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)




@client.event

async def on_ready():
    print("egro")

client.run("MTEzMDkxODkxNTcyMDEwMTk5OQ.G3Rsw0.PqHGs3BjZiiPKYD_1cqZlLUlrNQQEKIXHrp1cs")
