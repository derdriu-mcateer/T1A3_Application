from colorama import Fore
from date import date_today, check_date
from coffee_selection import CoffeeSelection
from coffee_machine import CoffeeMachine
import user_interface

user_interface.clear()
user_interface.welcome_greeting()

def main():
    coffee_machine = CoffeeMachine()
    check_date()
    while True:
        user_interface.user_menu()
        user_action = input("\n:")
        user_interface.clear()
        match user_action:
            case "5":
                user_interface.clear()
                # turn machine off
                # add the date into the txt file
                date_today()
                user_interface.goodbye_message()
                break
            case "4":
                user_interface.clear()
                # run the clean cycle function
                coffee_machine.cleaning_cycle()
            case "3":
                user_interface.clear()
                coffee_machine.supplies_report()
                # run the supplies report function
            case "2":
                user_interface.clear()
                # run the refill machine function
                coffee_machine.refill_machine()
            case "1":
                user_interface.clear()
                # run the coffee selection function then the make coffee function
                CoffeeSelection().user_menu()
                CoffeeSelection().user_selection()
                coffee_machine.make_coffee()
            case _:
                print(
                    f"\n{Fore.RED}Sorry [{user_action}] is not a valid option - please select a valid option"
                )

if __name__ == '__main__':
    main()
