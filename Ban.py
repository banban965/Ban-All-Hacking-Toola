#Downloder
import os
os.system('clear')
os.system ('pip install colorama')
#Os Clear For Termux
os.system('clear')
#Import
import colorama
import random
import sys
import time
import datetime
#From
from colorama import *
#Slow Print Def
def sp(text, delay=0.02):
    for char in str(text):
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
#Slow Input Def
def si(text, delay=0.02) :
    for char in str(text) :
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()
#Random Port And Tunnel And...
Port = random.randint(1024, 10240)
TLine = random.randint(1, 1000000)
DataN = random.randint(1, 99)
YourL = random.randint(1, 999)
CodeL = random.randint(999, 99999)
#Logs Viewer
sp (Fore.GREEN + "[Server]All Script Find...")
print ('')
sp (Fore.GREEN + "[Server]Port Is Running...")
print ('')
sp (Fore.GREEN + f"[Server]Port Is [{Port}]")
print ('')
sp (Fore.GREEN + "[Server]Tuunle Is Running...")
print ('')
sp (Fore.GREEN + f"[Server]Tuunle is [{TLine}]")
print ('')
sp (Fore.GREEN + "[Server]DataBase Is Running...")
print ('')
sp (Fore.GREEN + f"[Server]DataBase Is [{DataN}]")
print ('')
sp (Fore.GREEN + f"[Server]Your Line Is [{YourL}]")
print ('')
sp (Fore.GREEN + f"[Server]Code Line Is [{CodeL}]")
print ('')
sp (Fore.RED + "[System Logs] Loading...")
time.sleep(2)
os.system('clear')
#main menu
sp (Fore.YELLOW + "♧《《《《《》》》》》♧    ")
sp (Fore.YELLOW + "♧《《《ĤÃČ̣ĤÏÑĞ§》》》♧   ")
sp (Fore.YELLOW + "♧《《《《《》》》》》♧    ")
sp (Fore.RED + "1.Sms Bomber")
sp (Fore.RED + "2.Virus Crafter")
sp (Fore.RED + "3.Ddos Attacker")
sp (Fore.RED + "4.[RAT] Attack")
sp (Fore.RED + "5.Zphisher[App Attacker]")
sp (Fore.RED + "6.WI-FI Scanner")
sp (Fore.RED + "7.Bluetooth Scanner")
sp (Fore.RED + "8.File Browser")
sp (Fore.RED + "9.Ping Tester")
sp (Fore.RED + "10.Mini Game V¹")
sp (Fore.RED + "11.Mini Game V²")
sp (Fore.RED + "12.Exit")
sp (Fore.YELLOW + "♧《《《《《》》》》》♧    ")
User = si (Fore.GREEN + "ßelect Ɲumbers : ")
os.system('clear')
#if, elif and else
if User == "1":
    os.system('python SmsBomber/SmsBomber.py')
    
elif User == "2":
    os.system('bash VirusCrafter/TigerCrafter.sh')
    
elif User == "3":
    os.system('python ddos/ddos.py')
    
elif User == "4":
    os.system('python RAT/RAT.py')
    
elif User == "5":
    os.system('bash zphisher/zphisher.sh')
    
elif User == "6":
    os.system('bash WS/WI-FISC.sh')
    
elif User == "7":
    os.system('bash BS/BLUTOOTHS.sh')
    
elif User == "8":
    os.system('python MyFile/Run.py')
    
elif User == "9":
    os.system('python ST/SPEEDTEST.py')
    
elif User == "10":
    os.system('python MG1/1.py')
    
elif User == "11":
    os.system('python MG2/2.py')
     
elif User == "12":
    os.system('python Exit.py')
    
else:
    os.system('clear')
    sp (Fore.RED + "UNKNOWN NUMBER OR TEXT")
    sys.exit()
    
#made by BanBan445M
#BanBan445M = Mehrdad Mohamadzade
#made in iran 🇮🇷
#good byle
#@BanBan445M5M
#create by Mehrdad#create by Mehrdadadadddadadadd