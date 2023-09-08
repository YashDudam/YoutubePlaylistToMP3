#!/bin/bash

location="$1"
playlistURL="$2"

python3 -m venv env &&
source env/bin/activate &&
pip install -r requirements.txt &&
python3 convert.py "$location" "$playlistURL"