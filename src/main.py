from datetime import datetime
import date
from coffee_machine import CoffeeMachine

# The user interface 
def check_date():
    if date.past_date == str(datetime.now().date()):
        pass
    else:
        pass #will run a clean cycle

def main():
    coffee_machine = CoffeeMachine()
    machine_is_on = True

    while machine_is_on == True:
        user_action = input('Please select an option: [1] Make a coffee, [2] Refill the machine, [3] View Supply levels [4] Clean Machine, [5]Quit ')
        match user_action: 
            case '5':
                # turn machine off
                machine_is_on = False
                # add the date into the txt file
                date.date_today()
                print('Goodbye - have a lovely day')
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
                pass
            case _:
                print('Sorry that option is not valid - please select a valid option')


check_date()
main()