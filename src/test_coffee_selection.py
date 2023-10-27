from coffee_selection import CoffeeSelection
import pytest

# Testing that the user input will return the correct dictionary
coffee_pass = CoffeeSelection()


# If user inputs 1 then the dictionary for key 1 (Latte) will be returned
def test_user_selection_latte():
    selection = "1"
    choice = coffee_pass.coffee_types[selection]
    assert choice == {"name": "Latte", "water": 60, "coffee": 24, "milk": 90}


# If user inputs 2 then the dictionary for key 1 (Flat White) will be returned
def test_user_selection_FW():
    selection = "2"
    choice = coffee_pass.coffee_types[selection]
    assert choice == {"name": "Flat White", "water": 60, "coffee": 24, "milk": 180}


# If user inputs 3 then the dictionary for key 1 (Cappuchino) will be returned
def test_user_selection_Cap():
    selection = "3"
    choice = coffee_pass.coffee_types[selection]
    assert choice == {"name": "Cappuccino", "water": 60, "coffee": 24, "milk": 120}


# If user inputs 4 then the dictionary for key 1 (Long Black) will be returned
def test_user_selection_LB():
    selection = "4"
    choice = coffee_pass.coffee_types[selection]
    assert choice == {"name": "Long Black", "water": 180, "coffee": 24, "milk": 0}


# If user inputs 5 then the dictionary for key 1 (Espresso) will be returned
def test_user_selection_ES():
    selection = "5"
    choice = coffee_pass.coffee_types[selection]
    assert choice == {"name": "Espresso", "water": 60, "coffee": 20, "milk": 0}


coffee_fail = CoffeeSelection()


# If user inputs 6 then the a exception (KeyError) will be raised
def test_user_selection_no():
    selection = 6
    with pytest.raises(KeyError):
        choice = coffee_fail.coffee_types[selection]


# If user inputs a string then the a exception (KeyError) will be raised
def test_user_selection_no():
    selection = "a"
    with pytest.raises(KeyError):
        choice = coffee_fail.coffee_types[selection]
