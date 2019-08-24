import discord
from playsound import playsound
from discord.ext.commands import bot
from discord.ext import commands
import winsound
from time import sleep
import math,time


bot = commands.Bot(command_prefix= "!")
print("PRINTING SETTINGS...")
time.sleep(5)
token = open(r"token.txt","r").readline()
print(token)
serverid = open(r"serveridfile.txt","r").readline()
print(serverid)

@bot.event
async def on_ready():
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    print("(© = Created) | DiscordOBS ©2019, Wooystun#0005 - Creator: LazyNeko (˃ᆺ˂)#5644 - Helped With some stuff, especially related to .txt files:  Version 0.1.")
    print("Api Info: Discord.py 0.16.12 ©2016, Tkinter(Windows) ©2001-2019, PyQt5 © 2016 – 2019")
    print("This Code IS Open sourceable.")

@bot.event
async def on_disconnect():
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    print("!!!!!ALERT, ALERT, SCRIPT OFFLINE!!")

@bot.event
async def on_member_join(member):
    server = member.server
    owner = server.owner

    if server.id == serverid:
        playsound(r"Audio_1.mp3.mp3")


try: 
    bot.run(token)
except:
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    print("!!!!!ALERT, ALERT, SCRIPT OFFLINE!!")
    time.sleep(60)
    print("window closing soon...")
