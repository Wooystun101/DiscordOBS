import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions
from discord.utils import get
import discord.client
from collections import defaultdict
from asyncio import sleep
import asyncio
import math,time
import os
import sys
from os import system
from time import sleep
import aiohttp
import requests
from time import strftime
import datetime
from playsound import playsound
import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
#from TTK import Label
from PIL import Image, ImageTk
from tkinter.font import Font
import winsound



Client = discord.Client()
bot = commands.Bot(command_prefix= "!")
token = open(r"token.txt","r").readline()
serverid = open(r"serveridfile.txt","r").readline()
font = open(r"font.txt", "r").readline()
size = open(r"size.txt", "r").readline()
msg = open(r"message.txt").readline()
long = open(r"long.txt", "r").readline()
userid = open(r"useridfile.txt", "r").readline()

    
    
class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(r"animation1.gif.gif")
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass
        
        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)
        
    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)
        
    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)
        
    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)




@bot.event
async def on_ready():
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    print("(© = Created) DiscordOBS ©2019, Wooystun#0005 - Creator: LazyNeko (˃ᆺ˂)#5644 - Helped With some stuff, especially related to .txt files:  Version 0.1.")
    print("(© = Copyright)Api Info: Discord.py 0.16.12 ©2016, Tkinter(Windows) ©2001-2019, PyQt5 © 2016 – 2019")
    print("This Code IS Open sourceable.")


@bot.event
async def on_member_join(member):
    server = member.server
    owner = server.owner


    
    if server.id == serverid:
        file1 = open(r"text.txt","w")
        file1.write(member.name + "#" +  member.discriminator + " Joined the discord server!! Thank You :D")
        file1.close

        

    if __name__ == "__main__":
        from tkinter import Tk, Label

        w = tkinter.Tk()
        text = tkinter.Text(w)
        w.after(int(long), w.destroy)
        myFont = Font(family=font, size=size)
        text.configure(font=myFont)
    
        l = AnimatedGIF(w, r"animation1.gif.gif")
        Label(w, text= member.name + "#" +  member.discriminator + ' ' + msg).pack()
        l.pack()

    

        w.mainloop()

@bot.event
async def on_message(message):
    member = message.author
    user = member
    if user.id == userid:
        if message.content == "!configwindow":
            #async
            await bot.send_message(member, "configuring...")
            #rewrite
            #await member.send("configuring...")

            w = tkinter.Tk()
            text = tkinter.Text(w)

            l = AnimatedGIF(w, r"animation1.gif.gif")
            Label(w, text= "CONFIGURE THIS IN OBS").pack()
            l.pack()

            #member.name + "#" +  member.discriminator + " Joined the Discord Server!! Thank You ♥ "
    

            w.mainloop()
        


        
try: 
    bot.run(token)
except:
     winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
     print("!!!!!ALERT, ALERT, SCRIPT OFFLINE!!")
     time.sleep(60)
     print("window closing soon...")
