# T1A3 - Terminal Application

## GitHub Repository
The link for the Terminal Application GitHub repository can be found [here](https://github.com/mini109/T1A3_Application/tree/main)

## Help Documentation

### System / Hardware Requirements


### Software Requirements
#### Python 3
This application requires a Python version of 3 or higher. 

You can check if you have python installed by entering python --version into your terminal. 

Please visit [python.org](https://www.python.org/downloads/) if you do not have python installed or have a version of python older than Python 3. 

#### Pip 3
This application requires the lastest pip version available which is pip 3.

Pip should be installed when follow the Installation instructions.

However if you wish to download or upgrade pip onto your system now please visit [pip.pypa.io](https://pip.pypa.io/en/latest/getting-started/)



### Installation
#### GIT Clone
1. Follow the [link](https://github.com/mini109/T1A3_Application/tree/main) to the repository for this terminal application. 
2. Click the green < > Code button 
3. Under HTTPS - copy the https:// link \
![Installation with https clone](./docs/installation%20screenshots/clone_install.png)
4. In the terminal navigate into the folder where you would like the file to cloned into 
5. Clone the github repository by pasting the copied link 
```md 
git clone https://github.com/mini109/T1A3_Application.git
```
6. Navigate into the cloned folder (T1A3_Application)
7. Type BASH COMMAND to install the requirements and then BASH COMMAND to run the application

#### ZIP File 
1. Follow the [link](https://github.com/mini109/T1A3_Application/tree/main) to the repository for this terminal application.  
2. Click the green < > Code button
3. Click Download ZIP \
![Installation with zip file](./docs/installation%20screenshots/zip_install.png)
4. Extract the ZIP file and store the folder where you would like to house the application
5. In the terminal, navigate to the extracted ZIP FILE
6. Type BASH COMMAND to install the requirements and then BASH COMMAND to run the application

#### Using Code Spaces
1. Follow the [link](https://github.com/mini109/T1A3_Application/tree/main) to the repository for this terminal application. 
2. Click the green < > Code button
3. Click the Codespaces tab 
4. Click the Create codespace on main button \
![Installation with Codespaces](./docs/installation%20screenshots/codespace_install.png)
5. In the terminal within the codespace, Type BASH COMMAND to install the requirements and then BASH COMMAND to run the application


### Required Dependencies
### Walk Through
Below is a quick walkthrough of the coffee machine simulation for the terminal view. 



## Implementation Plan
Trello was used as the project management platform for this implementation plan. To view the trello board, please follow this [link](https://trello.com/invite/b/OaPuAP6S/ATTI2613cf6daa256cbdb98c4c141b9f8e119A3EC4AE/t1a3-terminal-app)

I organised my Trello board into 5 categories. 
- TO BE COMPLETED (tasks that have yet to be implemented)
- IN PROGRESS (tasks that are in the process of being completed)
- DONE  (tasks that have been completed successfully)
- ON GOING (tasks that a required to be constantly considered)
- IF TIME PERMITS (tasks that would be great to execute but not vital to the terminal application)

I also used labels within the Trello board to identify which tasks related to which category.\
![trello labels](./docs/trello%20screenshots/trello_labels.png)


I found it quite hard to implement date deadlines to each tasks so I decided to implement a grade of diffuculty to each task as this gave me a better idea of how long I thought a task may take me. 

I used a purple label to identify the FEATURES within the application. For each feature card I then created a checklist which provided an overview of the functions each feature should have. 

![features & checklists](./docs/trello%20screenshots/features.png)


## Features
### 1. Main Interface 
### 1. Coffee Menu Feature
### 2. Make a Coffee Feature
### 3. Refill Feature 
### 4. Report Feature
### 5. Cleaning Cycle Feature 
### 6. Turn off Feature 


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

[ascii banner](https://manytools.org/hacker-tools/ascii-banner/)
[ascii icon](https://www.asciiart.eu/image-to-ascii)