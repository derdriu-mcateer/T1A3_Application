import colorama
import user_interface
import time
from colorama import Fore
colorama.init(autoreset=True)


# stops colour from continuing
colour_close = "\033[39m"


class CoffeeSelection:
    def __init__(self):
        self.coffee_types = {
            "1": {"name": "Latte", "water": 60, "coffee": 24, "milk": 90},
            "2": {"name": "Flat White", "water": 60, "coffee": 24, "milk": 180},
            "3": {"name": "Cappuccino", "water": 60, "coffee": 24, "milk": 120},
            "4": {"name": "Long Black", "water": 180, "coffee": 24, "milk": 0},
            "5": {"name": "Espresso", "water": 60, "coffee": 20, "milk": 0},
        }

    def user_menu(self):
        print("\n Please select which type of coffee you would like to make: ")
        for key, value in self.coffee_types.items():
            print(
                f'''\n{Fore.YELLOW + "[" + str(key) + "]" + colour_close} {value["name"]}'''
            )

    def user_selection(self):
        while True:
            try:
                selection = input("\n:")
                choice = self.coffee_types[selection]
                return choice
            except (KeyError):
                print(f"\n{Fore.RED}Sorry [{selection}] is not a valid option")
                time.sleep(2)
                user_interface.clear()
                self.user_menu()
                continue
