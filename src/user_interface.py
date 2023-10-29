import time
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)


colour_close = "\033[39m"


def welcome_greeting():
    print(f'''\n {Fore.GREEN}TURNING ON \n''')
    time.sleep(1)
    with open("welcome_banner.txt", "r") as file:
        welcome = file.read()
    print(welcome)
    time.sleep(2)


def goodbye_message():
    with open("quit_banner.txt", "r") as file:
        goodbye = file.read()
    print(goodbye)
    time.sleep(2)
    print(f"\n {Fore.RED}TURNING OFF")
    time.sleep(1)


def user_menu():
    clear()
    print("\n Please select an option:")
    print(f'''\n{(Fore.YELLOW + '[1]' + colour_close)} Make A Coffee''')
    print(f'''\n{(Fore.YELLOW + '[2]' + colour_close)} Refill the Machine ''')
    print(f'''\n{(Fore.YELLOW + '[3]' + colour_close)} View Supply Levels ''')
    print(f'''\n{(Fore.YELLOW + '[4]' + colour_close)} Clean the Machine ''')
    print(f'''\n{(Fore.YELLOW + '[5]' + colour_close)} Turn Off''')


def clear():
    os.system("cls" if os.name == "nt" else "clear")
