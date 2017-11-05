#!/bin/bash

# this script is for deploying the eamon app

# python stuff
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

cd terranok-theme/static
npm install
npm build-css:upgrade
