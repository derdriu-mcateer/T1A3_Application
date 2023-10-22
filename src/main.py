from datetime import datetime
import date

# The user interface 
def check_date():
    if date.past_date == str(datetime.now().date()):
        pass
    else:
        date.date_today()
        print(('TODAYS DATE ADDED TO TXT FILE','orchid')) #this will be added to the quit function section of the main 

def main():
    pass



check_date()
main()