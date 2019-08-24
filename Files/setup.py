import subprocess
import sys
import os
import math,time
from os import system
from time import sleep


def install_function(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

print("Hi!! Welcome To The Python Discord Bot Join notification program for obs!!")
print("A Few Things First")
print("---")
time.sleep(1)
print("1. This Is Open Source!! The Files are included in a folder you downloaded")
time.sleep(1)
print("2. Please Name Your Audio.mp3, This Will clear up confusion for the program")
time.sleep(1)
print("3.  Please Name Your Gif Animation_1.gif")
time.sleep(1)
print("Thats It For Part 1!!")

time.sleep(3)
print(" ")
print("setup.py Is Starting....")
print(" ")
time.sleep(5)



pipqu = input("Do You Have Pip Installed (You would know if you have pip installed because You needed to run a get-pip.py file, which the installer can run if you dont have it installed. If you still want to double check, you can open cmd and type PIP In And you will know if it works)") 
if pipqu == 'no' or pipqu == 'No':
    print("The Installer will run the Get-pip.py file for you. You will however need to finish this by adding pip to path. You Can Do This by going to Control Panel > System And Security > System > Advanced System Settings > Environment Variables > Path. Then, Click New And Type In C:\Python(Version)\Scripts. Version Goes Your Version number without a point inbetween. So for example, if you have python 3.5, it will be  C:\Python35\Scripts. If You installed python from the installer included, it will be C:\Python36\Scripts.")
    print(" ")
    print("ALSO, IF YOU HAVENT ALRIGHTY, PLEASE READ THE INCLUDED README FILE!!!!")
    print("ALSO, IF YOU HAVENT ALRIGHTY, PLEASE READ THE INCLUDED README FILE!!!!")
    print("ALSO, IF YOU HAVENT ALRIGHTY, PLEASE READ THE INCLUDED README FILE!!!!")
    print("ALSO, IF YOU HAVENT ALRIGHTY, PLEASE READ THE INCLUDED README FILE!!!!")
    print(" ")
    print("Starting Get-pip.py (Instalation will start in 5 seconds")
    time.sleep(5)

    import getpip
    
    print("Sucessfully Installed Get-pip.py!")
    print(" ")
else:
    print("Skipping install of get-pip.py.")
    print(" ")


print("Testing modules...")
install_function("discord.py[voice]==0.16.12")
install_function("asyncio")
install_function("requests")
install_function("playsound")
install_function("aiohttp")

print("Success!!")
print(" ")

time.sleep(3)

print("general setup starting in... 5 Seconds")
print(" ")
time.sleep(5)
print("setup starting...")
print(" ")




#1
serverid = input("what is your server id? ")
print(serverid)
serveridfile = open(r"serveridfile.txt", "w")
serveridfile.write(serverid)
serveridfile.close()

print(" ")

#2
userid = input("What Is Your User ID? ")
print(userid)
useridfile = open(r"useridfile.txt", "w")
useridfile.write(userid)
useridfile.close()

#3
tokenin = input("what is The Token For Your Discord Bot? ")
token = open(r"token.txt", "w")
token.write(tokenin)
token.close()

print(" ")

font = input("What font would you like to use? ")
fontin = open(r"font.txt", "w")
fontin.write(font)
fontin.close

print(" ")

#4
size = input("What size do you want the font to be? ")
sizein = open(r"size.txt", "w")
sizein.write(size)
sizein.close()

print(" ")

#5
print("What would you like the message to say ")
msg = input("This Will Show up after a member.name + member.discriminator (ex: Tobu Clone#4788 [Message]) ")
message = open(r"message.txt", "w")
message.write(msg)
message.close()

print(" ")

 #6     
ask = input("Are you using custom audio? ")
if ask == 'yes' or ask == 'Yes':
    length = input("How Long Is The Custom audio? Also, Pls remember that it must be the length plus 3 zeros. Ex, 1 second = 1000, 5 seconds = 5000, 10 seconds = 10000, etc: ")
    long = open(r"long.txt", "w")
    long.write(length)
    long.close()
else:
    print("If You do plan on putting in a custom audio file, 3 things: 1. Please name it Audio_1.mp3. 2. Please repeat the setup to change this. 3, it needs to have 3 zeros after it. So Ex, 1 Second = 1000, 5 seconds = 5000, 10 Seconds = 10000, 15 = 15000: ")
    long = open(r"long.txt", "w")
    long.write("10000")
    long.close()

print(" ")



print("for the final step of the setup, You will have to trigger the event yourself, by making someone join, And open A New window capture in obs, and window capturing the new window opened when someone joins. ")

print(" ")

print("testing the contents of the .txt files...")
print(" ")
time.sleep(1)


f = open(r"serveridfile.txt", "r")
file_contents = f.read()
print ("Serverid:" + file_contents)
f.close()

print(" ")

f2 = open(r"useridfile.txt", "r")
file_content = f2.read()
print("Userid" + file_content)
f2.close()

print(" ")

f3 = open(r"token.txt", "r")
file_content = f3.read()
print("Token:" + file_content)
f3.close()

print(" ")

f4 = open(r"font.txt", "r")
file_content = f4.read()
print("font:" + file_content)
f4.close()

print(" ")

f5 = open(r"message.txt", "r")
file_content = f5.read()
print("Message:" + file_content)
f5.close()

print(" ")

f6 = open(r"long.txt", "r")
file_content = f6.read()
print("length of audio:" + file_content)
f6.close()


print(" ")

print("IF NOTHING SHOWED UP, PLEASE CONTACT THE DEVELOPER(Wooystun#0005) ON DISCORD. ")

print(" ")

print("Setup Complete! Now, Run The 2 RUN.BAT Files, 1 For Sound, And 1 for the gif, to use the obs Discord. ")

print(" ")

time.sleep(1)

print("Also, Please Use the command !configwindow, In the image script, to create a preview of the window. from here, you can put the gif into an obs window capture, and trigger it upon someone joining")

time.sleep(2)
print(" ")
print("Window closing in 5 seconds...")
time.sleep(5)
print("bye")




