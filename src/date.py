# will store all the functions relating to date and time
from datetime import datetime
from coffee_machine import CoffeeMachine


# Will read the date from the txt file (date the app was last accessed)
def accessed_date():
    try:
        with open("date_last_accessed.txt") as f:
            past_date = f.read()
        return past_date
    except FileNotFoundError as error:
        print(f"An error has occurred: {str(error)}")




# Will save current date into txt file once the app is quit
def date_today():
    with open("date_last_accessed.txt", "w") as f:
        current_date = str(datetime.now().date())
        f.write(f"{current_date}")
    return current_date


def check_date(past_date):
    if past_date != str(datetime.now().date()):
        CoffeeMachine().cleaning_cycle()  # will run a clean cycle
    else:
        pass


