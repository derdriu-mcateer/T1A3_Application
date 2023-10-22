from datetime import datetime
import date

# The user interface 
def check_date():
    if date.past_date == str(datetime.now().date()):
        pass
    else:
        pass #will run a clean cycle

def main():
    machine_is_on = True
    user_action = input('Please select an option: [1] Make a coffee, [2] Refill the machine, [3] Veiw Supply levels [4] Clean Machine, [5]Quit ')
    while machine_is_on == True:
        match user_action: 
            case '5':
                # turn machine off
                machine_is_on = False
                # add the date into the txt file
                date.date_today()
                pass
            case '4':
                # run the clean cycle function
                pass
            case '3':
                # run the supplies report function 
                pass
            case '2':
                # run the refill machine function 
                pass
            case '1':
                # run the coffee selection function then the make coffee function 
                pass


check_date()
main()