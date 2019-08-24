import subprocess
import sys
import os
import math,time
from os import system
from time import sleep


def install_function(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

print("OPEN AND RUN ME WITH IDLE")
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
    print("The Installer will run the Get-pip.py file for you.")
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

if pipqu == 'yes' or pipqu == 'Yes':
    print("Skipping install of get-pip.py.")
    print(" ")


print("Testing modules...")
install_function("discord.py[voice]==0.16.12")
install_function("asyncio")
install_function("requests")
install_function("PyQt5")
install_function("aiohttp")
install_function("pygame") 

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

print(" ")

#3
tokenin = input("what is your bots token? ")
token = open(r"token.txt", "w")
token.write(tokenin)
token.close()

print(" ")



#4
print("What would you like the message to say? ")
msg = input("This Will Show up after a member.name + member.discriminator (ex: Tobu Clone#4788 [Message]) ")
message = open(r"message.txt", "w")
message.write(msg)
message.close()

print(" ")

#5

Gif = input("Are You Using A Custom Gif? ")
if Gif == 'yes' or Gif == 'Yes':
    Wide = input("In Order To Determine The Window Size, We Need the Dementions of your gif. If You Double Click, And Go To GET INFO, Under the first line of MORE INFO: It should Say: Dimensions: number1 x number2. What Does Number 1, The One To The Left of The X say?")
    Width = open(r"Left.txt", "w")
    Width.write(Wide)
    Width.close()

    print(" ")

    Lengthe = input("And What Does number2, The One To the Right of the X Say?")
    Length = open(r"Right.txt", "w")
    numbers = [int(Lengthe), 46]
    numbersSum = sum(numbers, 1)
    print(numbersSum)
    Length.write(str(numbersSum))
    Length.close()

    print(" ")
else:
    print("If You Do Ever Decide To Put in A Custom gif, It is reccomended that you repeat the setup, as The Dimentions for the window are optimized under the defualt gif, And Not Your Custom gifs Dimentions")
    Width = open(r"Left.txt", "w")
    Width.write("480")
    Width.close()

    Length = open(r"Right.txt", "w")
    Length.write(str(264 + 46))
    Length.close()


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
print ("Serverid: " + file_contents)
f.close()

print(" ")

f2 = open(r"useridfile.txt", "r")
file_content = f2.read()
print("Userid: " + file_content)
f2.close()

print(" ")

f3 = open(r"token.txt", "r")
file_content = f3.read()
print("Token: " + file_content)
f3.close()

print(" ")

f4 = open(r"message.txt", "r")
file_content = f4.read()
print("Message: " + file_content)
f4.close()

print(" ")

f5 = open(r"long.txt", "r")
file_content = f5.read()
print("length of audio: " + file_content)
f5.close()

print(" ")

f6 = open(r"Left.txt", "r")
file_content = f6.read()
print("Length Of Gif: " + file_content)
f6.close()

print(" ")

f7 = open(r"Right.txt", "r")
file_content = f7.read()
print("Hight of gif: " + file_content)
f7.close()


Defualt = open(r"name.txt", "w")
Defualt.write("Defualt")
Defualt.close()


print(" ")

print("IF NOTHING SHOWED UP, PLEASE CONTACT THE DEVELOPER(Wooystun#0005) ON DISCORD. ")

print(" ")

print("Setup Complete! Now. To Configure It, Run The CONFIG.PY Script, And Use the Command !configwindow To Make A Window Show up. Then, Drop The window in an OBS Window capture, And Then Your Ready To Go. A")

print(" ")

time.sleep(1)

print("It Is Also Reccomended That You Rerun The Run.Py Script (The script your supposed to run after your done w/ setup(Setup.py), Which you pretty much are, And The Script for configulating it in obs (Config.py)) Each Time Someone Joins.")

print(" ")

print("Thats It, Enjoy!! Also, please Report any bugs to Wooystun#0005 On Discord.")

print(" ")

time.sleep(2)
print(" ")
print("Window closing in 5 seconds...")
time.sleep(5)
print("bye")




