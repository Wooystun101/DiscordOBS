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
from PyQt5.QtWidgets import *
import pygame
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )






Client = discord.Client()
client = commands.Bot(command_prefix= "!")
token = open(r"token.txt","r").readline()
serverid = open(r"serveridfile.txt","r").readline()
msg = open(r"message.txt").readline()
long = open(r"long.txt", "r").readline()
userid = open(r"useridfile.txt", "r").readline()
left = open(r"Left.txt", "r").readline()
right = open(r"Right.txt", "r").readline()


        
def restart_function():
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

def restart_funct():
      os.execv('/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6', ['python'] + [r'run.py'])
  
        
class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.resize(QSize(int(left), int(right))) #left #right
        self.setAttribute(Qt.WA_TranslucentBackground)
        QTimer.singleShot(int(long), self.destroy)



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(int(left), int(right)) #left #right
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.startUIWindow()
        stuff = open(r"name.txt").readline()
        self.statusBar().showMessage(stuff + msg)
        QTimer.singleShot(int(long), self.destroy)
 
    



        self.movie = QMovie("animation1.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()


    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("DiscordOBS (Wooystun#0005 For Credits, Restart of script reccomended after a person joins")
        self.show()
        QTimer.singleShot(int(long), self.destroy)




    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
            #time.sleep(10)
            #restart_funct()
     
    
   
@client.event
@asyncio.coroutine
def on_ready():
    os.system('afplay /System/Library/Sounds/Funk.aiff')
    print("DiscordOBS ©2019, Wooystun#0005 - Creator: LazyNeko (˃ᆺ˂)#5644 - Helped With some stuff, especially related to .txt files:  Version 0.1. No support For Unicode Based names. Reccomended You Rerun This script each time someone joins.")
    print("Api Info: Discord.py 0.16.12 ©2016, Tkinter(Windows) ©2001-2019, PyQt5 © 2016 – 2019")
    print("This Code IS Open sourceable.")
    #restart_function()



    
    
@client.event
@asyncio.coroutine
def on_member_join(member):
    server = member.server
    owner = server.owner

    



    if server.id == serverid:
        membername = open(r"name.txt", "w")
        membername.write(member.name + "#" + member.discriminator + " ")
        membername.close()
        time.sleep(5)
    


    if server.id == serverid:
        time.sleep(14)
        pygame.mixer.init()
        pygame.mixer.music.load("Audio_1.mp3")
        pygame.mixer.music.play()


    if server.id == serverid:
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            w = MainWindow()
            w.show()
            sys.exit(app.exec_())
        

        

        
        


@client.event
@asyncio.coroutine
def on_message(message):
    member = message.author
    user = member
    channel = message.channel
    server = message.server

           


        
try: 
    client.run(token)
except:
     restart_funct()
     os.system('afplay /System/Library/Sounds/Sosumi.aiff')
    

