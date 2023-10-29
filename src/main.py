from colorama import Fore
from date import date_today, check_date, accessed_date
from coffee_selection import CoffeeSelection
from coffee_machine import CoffeeMachine
import user_interface as ui
import time


def main():
    # clear terminal screen
    ui.clear()
    ui.welcome_greeting()
    coffee_machine = CoffeeMachine()
    ui.clear()
    past_date = accessed_date()
    # check date in txt file and run clean cycle if necessary
    check_date(past_date)
    while True:
        ui.user_menu()
        user_action = input("\n:")
        match user_action:
            case "5":
                ui.clear()
                # turn machine off
                # add the date into the txt file
                date_today()
                ui.goodbye_message()
                break
            case "4":
                ui.clear()
                # run the clean cycle function
                coffee_machine.cleaning_cycle()
            case "3":
                coffee_machine.supplies_report()
                # run the supplies report function
            case "2":
                ui.clear()
                # run the refill machine function
                coffee_machine.refill_machine()
            case "1":
                ui.clear()
                # run the coffee selection function
                CoffeeSelection().user_menu()
                choice = CoffeeSelection().user_selection()
                # pass choice variable onto make_coffee
                coffee_machine.make_coffee(choice)
            case _:
                print(f'''\n{Fore.RED}Sorry [{user_action}] is not a valid option''')
                time.sleep(1)


main()
