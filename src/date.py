# will store all the functions relating to date and time
from datetime import datetime
from coffee_machine import CoffeeMachine


# Will read the date from the txt file (date the app was last accessed)
def accessed_date():
    try:
        global past_date
        with open("date_last_accessed.txt") as f:
            past_date = f.read()
        return past_date
    except FileNotFoundError as error:
        print(f"An error has occurred: {str(error)}")


accessed_date()


# Will save current date into txt file once the app is quit
def date_today():
    with open("date_last_accessed.txt", "w") as f:
        current_date = str(datetime.now().date())
        f.write(f"{current_date}")
    return current_date


def check_date():
    try:
        if past_date == str(datetime.now().date()):
            CoffeeMachine().cleaning_cycle()  # will run a clean cycle
    except (
        NameError
    ):  # if past_date is not defined then use current date as the past date
        past_date = str(datetime.now().date())
