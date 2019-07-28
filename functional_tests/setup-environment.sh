#!/usr/bin/bash

# Remove previous virtual environments
rm -rf virtualenv
rm -f activate

# Create a new virtual environment
python -m venv virtualenv

# Symbolically link the activate script
ln -s virtualenv/bin/activate

# Source the activate script
source activate

# Find out which python we are now using
which python

# Upgrade pip
pip install --upgrade pip

# Install needed dependencies
pip install selenium requests tldextract

pip install ipython

# deactivate the virtual environment
deactivate
