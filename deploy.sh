#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Install spacy language model
python -m spacy download en_core_web_sm

# Build a wheel for spacy to avoid an error in Azure deployment
pip wheel spacy -w ./wheelhouse

# Deploy the app to Azure Web App
az webapp up -n ProfanityCheck -g cusswords --sku B1 --logs

# Set the startup command for the app
az webapp config set -n ProfanityCheck -g cusswords --startup-file app.py

# Restart the app to activate the changes
az webapp restart -n ProfanityCheck -g cusswords


