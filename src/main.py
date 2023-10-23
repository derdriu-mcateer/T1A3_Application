from date import date_today, check_date
from coffee_selection import CoffeeSelection
from coffee_machine import CoffeeMachine
import user_interface
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def main():
    coffee_machine = CoffeeMachine()
    machine_is_on = True
    user_interface.welcome_greeting()
    while machine_is_on == True:
        check_date()
        user_interface.user_menu()
        user_action = input(':')
        match user_action:
            case '5':
                # turn machine off
                machine_is_on = False
                # add the date into the txt file
                date_today()
                user_interface.goodbye_message()
            case '4':
                # run the clean cycle function
                coffee_machine.cleaning_cycle()
            case '3':
                coffee_machine.supplies_report()
                # run the supplies report function
            case '2':
                # run the refill machine function
                coffee_machine.refill_machine()
            case '1':
                # run the coffee selection function then the make coffee function
                CoffeeSelection().user_menu()
                CoffeeSelection().user_selection()
                coffee_machine.make_coffee()
            case _:
                print(f'\n{Fore.RED}Sorry that option is not valid - please select a valid option')


main()
