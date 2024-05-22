#!/bin/bash

# Ensure Python and pip are available
python3 -m ensurepip --upgrade

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt
