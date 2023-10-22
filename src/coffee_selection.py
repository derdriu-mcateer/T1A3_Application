class CoffeeSelection:

    def __init__(self):
        self.coffee_types = {
            1: {'name': 'Latte', 'water': 60, 'coffee': 24, 'milk': 90},
            2: {'name': 'Flat White', 'water': 60, 'coffee': 24, 'milk': 180},
            3: {'name': 'Cappucino', 'water': 60, 'coffee': 24, 'milk': 120},
            4: {'name': 'Long Black', 'water': 180, 'coffee': 24, 'milk': 0},
            5: {'name': 'Espresso', 'water': 60, 'coffee': 20, 'milk': 0}
        }
    
    def user_menu(self):
        print(' Please select which type of coffee you would like to make: ')
        for key, value in self.coffee_types.items():
            print(f'{key}:{value['name']}')


coffee_user = CoffeeSelection()

coffee_user.user_menu()

