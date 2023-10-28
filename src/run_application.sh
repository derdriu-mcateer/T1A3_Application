#!/bin/bash

# Check that PYTHON3 is installed 
./python_setup.sh

# Check that pip3 is installed
./pip_setup.sh

# Create a virtual environment
./venv_setup.sh

#Install required packages
./package_install.sh

#Run the application
echo 'Initiating Coffee Machine'
python3 main.py