import os
from os import system, name
import os.path
import time
import sys
import random
import pyfiglet
from termcolor import colored, cprint
from datetime import datetime
from datetime import date
import time
import colorama

#Function for clearing the screen throughout the program
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')