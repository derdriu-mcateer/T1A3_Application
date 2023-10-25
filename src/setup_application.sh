#!/bin/bash

# Change directory to src folder
cd ./src

# Check that PYTHON3 is installed 
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 main.py
    else
        echo 'ERROR: 
        This program requires the updated version of PYTHON3 to be installed.
        To update your version please visit https://www.python.org/downloads/' >&2
        exit 1
    fi 
else
    echo 'ERROR: 
    This program requires PYTHON3 to be installed. 
    To install PYTHON3 please visit https://www.python.org/downloads/' >&2
    exit 1
fi

# Check that pip3 is installed
if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'ERROR: 
    This program required PIP3 to be installed.
    To install PIP3, please visit https://pypi.org/project/pip/' >&2
  exit 1
fi

echo 'Python3 & PIP3 are correctly installed.'

# Create a virtual environment
echo 'Now installing virtual environment'
python3 -m venv venv
source venv/bin/activate

#Install required packages
echo 'Installing required packages'
pip3 install -r requirements.txt 

#Set up complete - instruct on how to run the application
echo "Set Up Complete - To run application please type: bash run_application.sh "