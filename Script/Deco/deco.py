#!/usr/bin/env python3

# Python Script for stdout data through config file

import configparser
import sys
from os.path import expanduser

config = configparser.ConfigParser()

# Open file and  parsing
with open(expanduser('deco-config'), 'r', encoding='utf-8') as f:
    config.read_file(f)


data  = [x for x in config.sections()]

# Display element
for element  in data:
    c = config[element]['content']
    sys.stdout.write(f'{c}')
