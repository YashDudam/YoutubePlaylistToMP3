#!/usr/bin/env python3

import os

def clear():
    for file in os.listdir('data'):
        file_path = os.path.join('data', file)
        os.remove(file_path)