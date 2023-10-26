from coffee_machine import CoffeeMachine
from coffee_selection import CoffeeSelection
import pytest

testMachineHigh =  CoffeeMachine(water = 200)
testMachineLow = CoffeeMachine(water = 20)
def test_cleaning_cycle_High(capsys):
    testMachineHigh.cleaning_cycle()
    capture = capsys.readouterr()
    if testMachineHigh.water > 50:
        full_capture = capture.out.split('complete.')
        latest_capture = full_capture[-1]
        assert latest_capture == ' The machine is ready for use\n'
    else:
        full_capture = capture.out.split('available.')
        latest_capture = full_capture[-1]
        assert latest_capture == " Please refill the machine\n"

def test_cleaning_cycle_Low(capsys):
    testMachineLow.cleaning_cycle()
    capture = capsys.readouterr()
    if testMachineLow.water > 50:
        full_capture = capture.out.split('complete.')
        latest_capture = full_capture[-1]
        assert latest_capture == ' The machine is ready for use\n'
    else:
        full_capture = capture.out.split('available.')
        latest_capture = full_capture[-1]
        assert latest_capture == " Please refill the machine\n"


coffee_Pass = CoffeeSelection()
no_Coffee = CoffeeSelection()
def test_user_selection_latte():
    selection = 1
    choice = coffee_Pass.coffee_types[selection]
    assert choice == {"name": "Latte", "water": 60, "coffee": 24, "milk": 90}

def test_user_selection_FW():
    selection = 2
    choice = coffee_Pass.coffee_types[selection]
    assert choice == {"name": "Flat White", "water": 60, "coffee": 24, "milk": 180}

def test_user_selection_Cap():
    selection = 3
    choice = coffee_Pass.coffee_types[selection]
    assert choice == {"name": "Cappucino", "water": 60, "coffee": 24, "milk": 120}

def test_user_selection_LB():
    selection = 4
    choice = coffee_Pass.coffee_types[selection]
    assert choice == {"name": "Long Black", "water": 180, "coffee": 24, "milk": 0}

def test_user_selection_ES():
    selection = 5
    choice = coffee_Pass.coffee_types[selection]
    assert choice == {"name": "Espresso", "water": 60, "coffee": 20, "milk": 0}

def test_user_selection_no():
    selection = 6
    with pytest.raises(KeyError):
        choice = no_Coffee.coffee_types[selection]

