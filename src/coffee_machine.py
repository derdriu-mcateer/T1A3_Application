import coffee_selection

#Represents the coffee machine
class CoffeeMachine:
    def __init__(self):
        # supplies held by the coffee machine 
        self.supplies = {'water':1000, 'coffee':500, 'milk' : 800}
    
    def supplies_report(self):
        # print a report of the machine's supplies and each level
        print(f'Water: {self.supplies['water']}ml / 1000ml')
        print(f'Coffee Beans: {self.supplies['coffee']}g / 500g')
        print(f'Milk: {self.supplies['milk']}ml / 800ml')

    def cleaning_cycle(self):
        # reduce the machine's water supply by 50ml
        self.supplies['water'] -= 50
        print('The cleaning cycle is now complete. The machine is ready for use')

    def refill_machine(self):
        refill_selection = input('Which supply would you like to refill [1]Water [2]Coffee Beans [3]Milk [4]All: ')
        match refill_selection:
            case '1':
                self.supplies['water'] = 1000
                print(f'Water: {self.supplies['water']}ml / 1000ml')
            case '2':
                self.supplies['coffee'] = 500
                print(f'Coffee Beans: {self.supplies['coffee']}g / 500g')
            case '3':
                self.supplies['milk'] = 800
                print(f'Milk: {self.supplies['milk']}ml / 800ml')
            case '4':
                self.supplies['water'] = 1000
                self.supplies['coffee'] = 500
                self.supplies['milk'] = 800
                print(f'Water: {self.supplies['water']}ml / 1000ml')
                print(f'Coffee Beans: {self.supplies['coffee']}g / 500g')
                print(f'Milk: {self.supplies['milk']}ml / 800ml')
            case _:
                print('Invalid selection - No supplies have been refilled')

    def make_coffee(self):
        #function which takes the users selection from coffeeselection class and determins if there are enough supplies to make the selection
        if (self.supplies['water'] >= coffee_selection.choice['water']) and (self.supplies['milk'] >= coffee_selection.choice['milk']) and (self.supplies['coffee'] >= coffee_selection.choice['coffee']):
            self.supplies['water'] -= coffee_selection.choice['water']
            self.supplies['coffee'] -= coffee_selection.choice['coffee']
            self.supplies['milk'] -= coffee_selection.choice['milk']
            print(f'here is your {coffee_selection.choice['name']}')
            return
        else:
            print(f'Sorry there are not enough supplies in the machine to make a {coffee_selection.choice['name']}. Please refill the machine.')