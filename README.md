# T1A3 - Terminal Application

## GitHub Repository
The link for the Terminal Application GitHub repository can be found [here](https://github.com/mini109/T1A3_Application/tree/main)

## Help Documentation

### System / Hardware Requirements
- Operating System:
    - Windows 7-10 or 11
    - Mac OS X 10.11 or higher, 64-bit
    - Linux: RHEL 6/7, 64-bit (almost all libraries also work in Ubuntu)
- x86 64-bit CPU (Intel / AMD architecture)
- 4 GB RAM
- 5 GB free disk space

(March.J, 2023)
### Software Requirements
#### Python 3
This application requires a Python version of 3 or higher. 

You can check if you have python installed by entering `python --version` into your terminal. 

Please visit [python.org](https://www.python.org/downloads/) if you do not have python installed or have a version of python older than Python 3. 

#### Pip 3
This application requires the lastest pip version available which is pip 3.

Pip should be installed when follow the Installation instructions.

However if you wish to download or upgrade pip onto your system now please visit [pip.pypa.io](https://pip.pypa.io/en/latest/getting-started/)

#### Note for Window Users 
The applicatiopn is not supported by the standard windows terminal and requires an alternative such as the git bash terminal or a Windows Subsystem for Linux(WSL) in order to achieve functionality.

### Command Line Arguments 
The terminal will prompt the user for input in various functions. 

There will be menus displayed such as the one below which asks the user to selection an option:

![coffee menu feature](./docs/feature%20screenshots/Coffee%20Menu.png)

Only numerical inputs between 1 and 5 are considered valid inputs in these cases. 
```md 
1       2       3       4       5 
``` 
No other input will be accepted - any other input will display an error message and prompt the user to try again. 

There is also cases where the terminal will print `" Press any key to continue: "` here the user can provide any keyboard input and the application will proceed. 

![supply report feature](./docs/feature%20screenshots/Supplies%20Report.png)





### Installation
#### GIT Clone
1. Follow this [link](https://github.com/mini109/T1A3_Application/tree/main) to the github repository for this terminal application. 
2. Click the green < > Code button 
3. Under HTTPS - copy the https:// link 

![Installation with https clone](./docs/installation%20screenshots/clone_install.png)

4. In your terminal window navigate into the folder where you would like the file to be cloned into 
5. Clone the github repository by pasting the copied link 
``` md
git clone https://github.com/mini109/T1A3_Application.git
``` 
6. Navigate into the cloned folder (T1A3_Application) 
```md 
cd T1A3_Application
```
7. Naviagate into the src folder
```md 
cd src
```
7. Type in `bash run_application.sh` to install the requirements run the application
```md
bash run_application.sh
```

#### ZIP File 
1. Follow the [link](https://github.com/mini109/T1A3_Application/tree/main) to the repository for this terminal application.  
2. Click the green < > Code button
3. Click Download ZIP \
![Installation with zip file](./docs/installation%20screenshots/zip_install.png)
4. Extract the ZIP file and store the folder where you would like to house the application
5. In your terminal window, navigate to the extracted ZIP FILE
6. Naviagate into the src folder
```md 
cd src
```
7. Type in `bash run_application.sh` to install the requirements run the application
```md
bash run_application.sh


#### Using Code Spaces
1. Follow the [link](https://github.com/mini109/T1A3_Application/tree/main) to the repository for this terminal application. 
2. Click the green < > Code button
3. Click the Codespaces tab 
4. Click the Create codespace on main button \
![Installation with Codespaces](./docs/installation%20screenshots/codespace_install.png)
5. In the terminal within the codespace Naviagate into the src folder
```md 
cd src
```
6. Type in `bash run_application.sh` to install the requirements run the application
```md
bash run_application.sh
```


### Required Dependencies
- black==23.10.1
- clear-screen==0.1.14
- click==8.1.7
- colorama==0.4.6
- Columnar==1.4.1
- iniconfig==2.0.0
- markdown-it-py==3.0.0
- mdurl==0.1.2
- mypy-extensions==1.0.0
- packaging==23.2
- pathspec==0.11.2
- platformdirs==3.11.0
- pluggy==1.3.0
- pycodestyle==2.11.1
- Pygments==2.16.1
- pytest==7.4.2
- setuptools==68.2.2
- termact==0.0.2
- toolz==0.12.0
- wcwidth==0.2.8



## Implementation Plan
Trello was used as the project management platform for this implementation plan. To view the trello board, please follow this [link](https://trello.com/invite/b/OaPuAP6S/ATTI2613cf6daa256cbdb98c4c141b9f8e119A3EC4AE/t1a3-terminal-app)

I organised my Trello board into 5 categories. 
- TO BE COMPLETED (tasks that have yet to be implemented)
- IN PROGRESS (tasks that are in the process of being completed)
- DONE  (tasks that have been completed successfully)
- ON GOING (tasks that a required to be constantly considered)
- IF TIME PERMITS (tasks that would be great to execute but not vital to the terminal application)

I also used labels within the Trello board to identify which tasks related to which category.

![trello labels](./docs/trello%20screenshots/trello_labels.png)


I found it quite hard to implement date deadlines to each tasks so I decided to implement a grade of diffuculty to each task as this gave me a better idea of how long I thought a task may take me. 

I used a purple label to identify the FEATURES within the application. For each feature card I then created a checklist which provided an overview of the functions each feature should have. 

![features & checklists](./docs/trello%20screenshots/features.png)

Below are A FEW progress screenshots during the development of the terminal application. The history of the board can be viewed within the trello website. 

![progress 1](./docs/trello%20screenshots/progress_1.png)
![progress 2](./docs/trello%20screenshots/progress_2.png)
![progress 3](./docs/trello%20screenshots/progress_3.png)

## Features
### 1. Main Interface 
The main user interface is the feature the user will initially interact with upon initiating the application.

![main user interface](./docs/feature%20screenshots/Main%20Interface.png)

The user is presented with 5 options to select from. A match case statement is used to assess the user's input. Upon a successful match various functions are called to display the other features of the application. 

In the case that the user's input does not satisfy the match case statement then a red error message is displayed prompting the user to enter a valid input. 

Note that the match case statement is nested within a while loop. This while loop is only broken when the user enters '5' which quits the program eseentually simulating the turning off of a coffee machine. 
```python
    while True:
        user_interface.user_menu()
        user_action = input("\n:")
        match user_action:
            case "5":
                user_interface.clear()
                date_today()
                user_interface.goodbye_message()
                break
            case "4":
                user_interface.clear()
                coffee_machine.cleaning_cycle()
            case "3":
                coffee_machine.supplies_report()
            case "2":
                user_interface.clear()
                coffee_machine.refill_machine()
            case "1":
                user_interface.clear()
                CoffeeSelection().user_menu()
                choice = CoffeeSelection().user_selection()
                coffee_machine.make_coffee(choice)
            case _:
                print(f'''\n{Fore.RED}Sorry [{user_action}] is not a valid option''')
                time.sleep(1)
```

### 2. Coffee Menu Feature
Another main feature of the application is the menu feature which displays the types of coffee's the machine can output. There are 5 options that the user can select. 

![coffee menu feature](./docs/feature%20screenshots/Coffee%20Menu.png)

The different coffee types are stored within a nested dictionary which contains the name of the coffee type, the level of water, coffee and milk requirements to make the coffee. Within the coffee menu feature only the key(1,2,3 etc) and the name values are utilised. 

```python
class CoffeeSelection:
    def __init__(self):
        self.coffee_types = {
            "1": {"name": "Latte", "water": 60, "coffee": 24, "milk": 90},
            "2": {"name": "Flat White", "water": 60, "coffee": 24, "milk": 180},
            "3": {"name": "Cappuccino", "water": 60, "coffee": 24, "milk": 120},
            "4": {"name": "Long Black", "water": 180, "coffee": 24, "milk": 0},
            "5": {"name": "Espresso", "water": 60, "coffee": 20, "milk": 0},
        }
```

The menu is displayed to the user by using a for loop which iterates over the key-value pairs within self.coffee_types and displays the key and the name values. 

```python
    def user_menu(self):
        print("\n Please select which type of coffee you would like to make: ")
        for key, value in self.coffee_types.items():
            print(
                f'''\n{Fore.YELLOW + "[" + str(key) + "]" + colour_close} {value["name"]}'''
            )
```

The final function within this feature is the user_selection function where the user inputs their selection. A valid selection is an input which matches any of the 5 keys within the coffee_types dictionary. A choice variable is utilised to store the matched key's dictionary value. This is then accessed by the make_coffee function within a different class. 

Error handling is utilised here to print an error message should a KeyError occur. Using a while loop the user is shown the user_menu again and prompted to select a valid option. The while loop continues until the user selects a valid option. 
```python
    def user_selection(self):
        while True:
            try:
                selection = input('\n:')
                choice = self.coffee_types[selection]
                return choice
            except(KeyError):
                print(f'\n{Fore.RED}Sorry [{selection}] is not a valid option')
                time.sleep(2)
                user_interface.clear()
                self.user_menu()
                continue
```


### 3. Make a Coffee Feature
A key feature of the application is the feature which represents the output of a coffee. The function used within this feature is the make_coffee function within the CoffeeMachine class.

There are three conditions which must be satisfied for the IF statement to be executed. The conditions check that the machine's supply levels for water, milk & coffee are all greater than or equal to the selected coffee type's requirements. Please note that the machine's supply levels are stored within the constructor of the CoffeeMachine class and are accessed in the make_coffee function as self.water, self.milk and self.coffee. As previosuly mentioned in the Coffee Menu feature above, the user's valid input is used to create the choice variable which stores the matched key's dictionary value. This variable is utilised within the make_coffee function to access the chosen coffee type's requirements. 

Should all three conditions be TRUE then the function proceeds to minus the specified requirements of the coffee selection from the machine's supply levels. A series of print messages then occur to show the user that their coffee has been successfully made. 

In the case that the any of IF conditions are not satisfied then a red error message is displayed to the user prompting them to refill the machine. 

```python
    def make_coffee(self, choice):
        condition1 = self.water >= choice["water"]
        condition2 = self.milk >= choice["milk"]
        condition3 = self.coffee_beans >= choice["coffee"]
        if (condition1 and condition2 and condition3):
            self.water -= choice["water"]
            self.coffee_beans -= choice["coffee"]
            self.milk -= choice["milk"]
            user_interface.clear()
            print(f'''\n Preparing your {
                  (Fore.YELLOW + choice["name"] + colour_close)} - please wait ''')
            time.sleep(2)
            user_interface.clear()
            print(f'''\n Your {
                (Fore.YELLOW + choice["name"] + colour_close)} is now ready.''')
            with open("coffee_icon.txt", "r") as file:
                icon = file.read()
            print(icon)
            time.sleep(2)
            user_interface.clear()
        else:
            user_interface.clear()
            print(f'''\n{Fore.RED}Sorry there are not enough supplies in the machine to make a {
                  choice["name"]}. Please refill the machine.''')
            time.sleep(3)
```
### 4. Cleaning Cycle Feature 
Another feature within the terminal application is the cleaning cycle feature. This is represented by the cleaning_cycle function within the CoffeeMachine class. 

The cleaning cycle feature utilises an if/else statement and determines that if the machine’s water supply (self.water) is greater than 50. If this condition is true an initiating cleaning cycle message is printed on the terminal screen followed by a cleaning cycle completed message 3 seconds later. Also value of self.water is reduced by 50. However if the condition is false and self.water is less than 50 then an error message is displayed to the user and returns them to the main menu. 

```python
    def cleaning_cycle(self):
        if self.water > 50:
            print(f'\n{Fore.YELLOW}Initiating cleaning cycle - please standby')
            time.sleep(3)
            self.water -= 50
            print(f'\n{Fore.GREEN}The cleaning cycle is complete. The machine is ready for use')
            time.sleep(2)
        else:
            print(f'\n{Fore.RED}Unable to complete the cleaning cycle.\n')
            print('There is an insufficient amount of water available. Please refill the machine')
            time.sleep(2)
```

There are two intances that this feature can be displayed to the user. Firstly is if the user inputs '4' from the main interface then the cleaning_cycle function is run. The second is through the user of the check_function. 

The check_date function works alongside two other functions. Firstly the accessed_date function will open and read the date stored within the date_last_accessed.txt file. If there is no date within this file or the date doesn’t match the current date then the check_date function will run the cleaning cycle. The date is stored within the txt file through the execution of the date_today function. This function will open the txt file and write in the current date. The date_today function is executed when the user inputs '5' from the main interface. 

```python
def accessed_date():
    try:
        with open("date_last_accessed.txt") as f:
            past_date = f.read()
        return past_date
    except FileNotFoundError as error:
        print(f"An error has occurred: {str(error)}")

def date_today():
    with open("date_last_accessed.txt", "w") as f:
        current_date = str(datetime.now().date())
        f.write(f"{current_date}")
    return current_date

def check_date(past_date):
    if past_date != str(datetime.now().date()):
        CoffeeMachine().cleaning_cycle()  
    else:
        pass
```


## Styling
The source code for this terminal application adhered to the PEP 8 style guidelines. 

PEP 8 was chosen to enhance the clarity and consistency of the application's code.

Please note that the line length limit has been extended from 79 characters to 99 characters. As stated in the PEP 8 guidelines as long as all team members are in agreement the line length limit can be increased to 99 characters, however this excludes comments and docstrings which must still be limited to 72 characters. 

The PEP 8 style code for python code can be found [here](https://peps.python.org/pep-0008/)

## Testing
Testing was completed using PYTEST. It has been listed in the required dependencies.  

1. The first set of tests check that the user_selection function within the CoffeeSelection class works as intended. 
- The value assigned to the selection varaible represents the user input.
- The choice varaible is equal to the the dictionary value assigned to the selection varaible

- The expected outcome from the user inputting a correct selection is that the choice varaible will be equal to the dictionary value assigned to the selection varaible (All integers between 1 - 5 were tested to ensure they were returning the expected dictionary)
```python
def test_user_selection_latte():
    selection = 1
    choice = coffee_pass.coffee_types[selection]
    assert choice == {"name": "Latte", "water": 60, "coffee": 24, "milk": 90}
```

- The expected outcome from the user inputting an incorrect selection is that the a KEYERROR is returned
```python
def test_user_selection_no():
    selection = 6
    with pytest.raises(KeyError):
        choice = coffee_fail.coffee_types[selection]

def test_user_selection_no():
    selection = 'a'
    with pytest.raises(KeyError):
        choice = coffee_fail.coffee_types[selection]
```

- All tests passed as expected 
![Pytest Results from CoffeeSelection test](./docs/testing%20screenshots/test_coffee_selection.png)

2. The second set of tests check that the cleaning_cycle feature within the CoffeeMachine class works as intended.

- The cleaning_cycle feature will assertain if the water supply is above 50 then it will iniate a cleaning cycle where the machine will loose 50ml of water. If there is an insufficient water supply then an error message will appear and the water level is remain the same.
```python
    def cleaning_cycle(self):
        # reduce the machine's water supply by 50ml
        if self.water > 50:
            print(f'\n {Fore.YELLOW}Initiating cleaning cycle - please standby')
            time.sleep(3)
            self.water -= 50
            print(f'\n {Fore.GREEN}The cleaning cycle is now complete. The machine is ready for use')
            time.sleep(2)
        else:
            print(f'\n {Fore.RED}Unable to complete the cleaning cycle. \n There is an insufficient amount of water available. Please refill the machine')
            time.sleep(2)
```

- The first test checks the outcome when there is enough water in the machine to complete a cleaning cycle. I experienced some issues with PYTEST and the print statements within the cleaning_cycle function so I decided to use the split() function to check only the last print statement. The expected outcome of this test is that the lastest_capture is equal to the final print statement of the function and that water is now equal to 150. 
```python
testMachineHigh = CoffeeMachine(water=200)

def test_cleaning_cycle_High(capsys):
    testMachineHigh.cleaning_cycle()
    capture = capsys.readouterr()
    if testMachineHigh.water > 50:
        full_capture = capture.out.split("\n")
        latest_capture = full_capture[-2]
        # Pytest will read colorama text as ASNI sequences so (\x1b[32m is equal to FORE.GREEN)
        assert (
            latest_capture
            == " \x1b[32mThe cleaning cycle is now complete. The machine is ready for use"
        )
        assert testMachineHigh.water == 150
    else:
        full_capture = capture.out.split("\n")
        latest_capture = full_capture[-2]
        assert (
            latest_capture
            == " There is an insufficient amount of water available. Please refill the machine"
        )
```
- The second test case tests the outcome when the water supply is insuffient to complete a cleaning cycle (<50). As previously mentioned there was some issues with PYTEST and asserting the print statements so I decided to check only the last part of the print statement from the else statement. The expected outcome of this test is that the lastest_capture is equal to the last sentence in the print statement and that the water level remains unchanged. 

```python

testMachineLow = CoffeeMachine(water=20)

def test_cleaning_cycle_Low(capsys):
    testMachineLow.cleaning_cycle()
    capture = capsys.readouterr()
    if testMachineLow.water > 50:
        full_capture = capture.out.split("\n")
        latest_capture = full_capture[-2]
        assert (
            latest_capture
            == " \x1b[32mThe cleaning cycle is now complete. The machine is ready for use"
        )
    else:
        full_capture = capture.out.split("\n")
        latest_capture = full_capture[-2]
        assert (
            latest_capture
            == " There is an insufficient amount of water available. Please refill the machine"
        )
        assert testMachineLow.water == 20
```
- Both tests passed as expected
![Pytest Results from CoffeeMachine test](./docs/testing%20screenshots/test_coffee_machine.png)


## Refrences 
March, J. (2023). Enthought Python Minimum Hardware Requirements. [online] Enthought Knowledge Base. Available at: https://support.enthought.com/hc/en-us/articles/204273874-Enthought-Python-Minimum-Hardware-Requirements. 

“Create ASCII Text Banners Online.” Manytools.org - Your Online Toolshed, manytools.org/hacker-tools/ascii-banner/. [ascii banner](https://manytools.org/hacker-tools/ascii-banner/)

“Image to ASCII: Free ASCII Art Converter.” Image to ASCII: Free ASCII Art Converter, www.asciiart.eu/image-to-ascii. [ascii icon](https://www.asciiart.eu/image-to-ascii)

van Rossum, Guido, et al. “PEP 8 – Style Guide for Python Code | Peps.python.org.” Peps.python.org, 5 July 2001, https://peps.python.org/pep-0008/ 

“Bash Reference Manual.",  https://www.gnu.org/software/bash/manual/bash.html