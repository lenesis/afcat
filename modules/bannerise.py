from time import sleep
import platform
import os
import random
from colorama import init, Fore
init()

def __clear():
    if platform.uname()[0] == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    print (Fore.RED,r''' ________  ________ ________  ________  _________   
|\   __  \|\  _____\\   ____\|\   __  \|\___   ___\ 
\ \  \|\  \ \  \__/\ \  \___|\ \  \|\  \|___ \  \_|        version: 1.0
 \ \   __  \ \   __\\ \  \    \ \   __  \   \ \  \  
  \ \  \ \  \ \  \_| \ \  \____\ \  \ \  \   \ \  \         |\__/,|   (`\
   \ \__\ \__\ \__\   \ \_______\ \__\ \__\   \ \__\      _.|o o  |_   ) )
    \|__|\|__|\|__|    \|_______|\|__|\|__|    \|__|    -(((---(((--------
    ''','\n', Fore.RESET)

def load():
    __clear()
    loadg = [
        'Loading . ',
        'lOading : ',
        'loAding :.',
        'loaDing ::',
        'loadIng ::',
        'loadiNg :.',
        'loadinG : '
    ]
    print(f'''
    {Fore.LIGHTRED_EX}   o  .              
    {Fore.LIGHTRED_EX}  o O.       {Fore.LIGHTYELLOW_EX}         ᴛʜɪs ᴘʀᴏᴊᴇᴄᴛ ᴡᴀs
    {Fore.LIGHTRED_EX}  . o O      {Fore.LIGHTYELLOW_EX}         ᴍᴀᴅᴇ ᴡɪᴛʜ ʟᴏᴠᴇ ɪɴ
    {Fore.LIGHTRED_EX}     o       
    {Fore.LIGHTGREEN_EX} ┓  ┳┓┓  ┓    {Fore.LIGHTCYAN_EX}   ┏━ https://leNlabs.ir/gitproj ━┓
    {Fore.LIGHTGREEN_EX} ┃┏┓┃┃┃┏┓┣┓┏  {Fore.LIGHTCYAN_EX}   ┃                              ┃
    {Fore.LIGHTGREEN_EX} ┗┗ ┛┗┗┗┻┗┛┛  {Fore.LIGHTCYAN_EX}   ┗━ https://github.com/lenesis ━┛
    ''')
    i = 35
    j = 0
    while i > 0:
        print(Fore.LIGHTWHITE_EX, loadg[j], end='\r')
        sleep(.1)
        i -= 1
        if j != 6:
            j += 1
        else:
            j = 0
    __clear()
    banner()
