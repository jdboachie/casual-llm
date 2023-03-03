"""
Printer module
"""
from time import sleep
from random import randint


def type_it(text):
    """
    Prints text as if it were being typed by a human
    """
    for char in text:
        sleep(randint(1, 10)/100)
        print(char, end='', flush=True)
