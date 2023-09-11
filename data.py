#!usr/bin/env python3

import os

def clear():
    [ os.remove(f'./data/{file}') for file in os.listdir('./data') ]

def mkdata():
    if not (os.path.exists('./data') and os.path.isdir('./data')):
        os.mkdir('data')