#!usr/bin/env python3

import os

def clear():
    [ os.remove(f'./data/{file}') for file in os.listdir('./data') ]
