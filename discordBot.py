#invite link: https://discord.com/api/oauth2/authorize?client_id=1130918915720101999&permissions=26933437398081&scope=bot

# bot token: MTEzMDkxODkxNTcyMDEwMTk5OQ.G3Rsw0.PqHGs3BjZiiPKYD_1cqZlLUlrNQQEKIXHrp1cs

import discord
import os



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)




@client.event

async def on_ready():
    print("egro")

client.run("MTEzMDkxODkxNTcyMDEwMTk5OQ.G3Rsw0.PqHGs3BjZiiPKYD_1cqZlLUlrNQQEKIXHrp1cs")