import colorama
from colorama import Fore
colorama.init(autoreset=True)
import coffee_selection

#Represents the coffee machine
class CoffeeMachine:
    def __init__(self):
        # supplies held by the coffee machine 
        self.water = 500
        self.coffee_beans = 250
        self.milk = 300
    
    def supplies_report(self):
        # print a report of the machine's supplies and each level
        print(f'Water: {self.water}ml / 1000ml')
        print(f'Coffee Beans: {self.coffee_beans}g / 500g')
        print(f'Milk: {self.milk}ml / 800ml')

    def cleaning_cycle(self):
        # reduce the machine's water supply by 50ml
        self.water -= 50
        print(f'\n The cleaning cycle is now complete. The machine is ready for use')

    def refill_machine(self):
        refill_selection = input('Which supply would you like to refill [1]Water [2]Coffee Beans [3]Milk [4]All [5]None : ')
        match refill_selection:
            case '1':
                self.water = 500
                self.supplies_report()
            case '2':
                self.coffee_beans = 250
                self.supplies_report()
            case '3':
                self.milk = 400
                self.supplies_report()
            case '4':
                self.water = 500
                self.coffee_beans = 250
                self.milk = 400
                self.supplies_report()
            case '5':
                print('No supplies have been refilled')
            case _:
                print('Invalid selection - No supplies have been refilled')

    def make_coffee(self):
        #function which takes the users selection from coffeeselection class and determins if there are enough supplies to make the selection
        if (self.water >= coffee_selection.choice['water']) and (self.milk >= coffee_selection.choice['milk']) and (self.coffee_beans >= coffee_selection.choice['coffee']):
            self.water -= coffee_selection.choice['water']
            self.coffee_beans -= coffee_selection.choice['coffee']
            self.milk -= coffee_selection.choice['milk']
            print(f'here is your {coffee_selection.choice['name']}')
            return
        else:
            print(f'\n{Fore.RED}Sorry there are not enough supplies in the machine to make a {coffee_selection.choice['name']}. Please refill the machine.')