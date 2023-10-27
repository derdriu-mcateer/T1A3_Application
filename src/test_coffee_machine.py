from coffee_machine import CoffeeMachine
import pytest

# Testing the cleaning cycle function within the CoffeeMachine class.

testMachineHigh = CoffeeMachine(water=200)


# Testing the output when the machine's water level is sufficient
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


testMachineLow = CoffeeMachine(water=20)


# Testing the output when the machine's water level is insufficient
def test_cleaning_cycle_Low(capsys):
    testMachineLow.cleaning_cycle()
    # capture the output when the cleaning cycle function is called
    capture = capsys.readouterr()
    # will pass the if condition because the water level is below 50
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
