#!/bin/bash

# Create a virtual environment and activate it
python3 -m venv antenv
source antenv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Install Spacy data
python -m spacy download en_core_web_sm

# Run the application
gunicorn app:app -b 0.0.0.0:$PORT --timeout 600
