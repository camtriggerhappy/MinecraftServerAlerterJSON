import requests
import discord

file = open("../Token/Token.txt")
token = file.read()
file.close()
file = open("../Token/IP.txt")
IP = file.read()
file.close()

client = discord.client()

async def on_ready():
    print("Logged in")




@client.event
async def on_message():
    r = requests.get(f"https://api.mcsrvstat.us/2/{}")







client.run(token)