import time
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def welcome_greeting():
    print(f'\n {Fore.CYAN}Hello there!')
    

def goodbye_message():
    print(f'\n {Fore.RED}TURNING OFF')
    time.sleep(1)
    print(f'\n {Fore.CYAN}Goodbye - have a lovely day!')
    time.sleep(1)
    

def user_menu():
    time.sleep(1)
    print('\n Please select an option:')
    print(f'\n{(Fore.YELLOW + '[1]' + '\033[39m')} Make A Coffee')
    print(f'\n{(Fore.YELLOW + '[2]' + '\033[39m')} Refill the Machine ') 
    print(f'\n{(Fore.YELLOW + '[3]' + '\033[39m')} View Supply Levels ') 
    print(f'\n{(Fore.YELLOW + '[4]' + '\033[39m')} Clean the Machine ')
    print(f'\n{(Fore.YELLOW + '[5]' + '\033[39m')} Turn Off')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')