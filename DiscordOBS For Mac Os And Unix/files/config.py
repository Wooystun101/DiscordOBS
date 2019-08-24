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
stuff = open(r"name.txt").readline()


        
class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        self.resize(QSize(480, 310)) #left #right



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 600, 750)
        self.setFixedSize(480,310) #left #right
        self.startUIWindow()
        self.statusBar().showMessage(stuff + msg)
 
    



        self.movie = QMovie("animation1.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()


    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("DiscordOBS (Wooystun#0005 For Credits, Restart of script reccomended after a person joins")
        self.show()




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
    print("DiscordOBS ©2019 - Configulation (© = Creation, not copyright lol)")
    #restart_function()



    

        

        
        


@client.event
@asyncio.coroutine
def on_message(message):
    member = message.author
    user = member
    channel = message.channel
    server = message.server

            
    if user.id == userid:
        if server.id == serverid:
            if message.content == "!configwindow":
     
                yield from client.send_message(message.channel, "Move Quick, You Only Have 10 seconds!")
                yield from client.send_message(member, "configuring...") 
   

                app = QApplication(sys.argv)
                t = MainWindow()
                t.show()
                sys.exit(app.exec_())

           


        
try: 
    client.run(token)
except:
     restart_funct()
     os.system('afplay /System/Library/Sounds/Sosumi.aiff')
    

