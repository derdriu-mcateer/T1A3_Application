#!/bin/bash

# Change directory to src folder
cd ./src

# Check that PYTHON3 is installed 
python_setup.sh

# Check that pip3 is installed
pip_setup.sh

# Create a virtual environment
venv_setup.sh

#Install required packages
package_install.sh

#Set up complete - instruct on how to run the application
echo "Set Up Complete - To run application please type: bash run_application.sh "

#Run the application
echo 'Initiating Coffee Machine'
python3 main.py