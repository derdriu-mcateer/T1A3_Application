# Check that PYTHON3 is installed 
if [[ -x "$(command -v python)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        echo 'Python 3 is correctly installed.'
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
