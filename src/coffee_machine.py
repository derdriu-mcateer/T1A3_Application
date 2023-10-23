# Represents the coffee machine
class CoffeeMachine:
    def __init__(self):
        # supplies held by the coffee machine 
        self.supplies = {'water':1000, 'coffee':500, 'milk' : 800}
    
    def supplies_report(self):
        # print a report of the machine's supplies and each level
        print(f'{self.supplies['water']}')
        print(f'{self.supplies['coffee']}')
        print(f'{self.supplies['milk']}')

    def cleaning_cycle(self):
        # reduce the machine's water supply by 50ml
        self.supplies['water'] -= 50
        print('The cleaning cycle is now complete. The machine is ready for use')
        return

    def refill_machine(self):
        pass

    def make_coffee(self):
        pass