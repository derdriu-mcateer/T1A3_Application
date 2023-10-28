# Check that pip3 is installed
if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'ERROR: 
    This program required PIP3 to be installed.
    To install PIP3, please visit https://pypi.org/project/pip/' >&2
  exit 1
fi

echo 'PIP3 is correctly installed.'