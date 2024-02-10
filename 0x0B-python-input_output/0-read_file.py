#!/usr/bin/python3
"""defing read_file function"""


def read_file(filename=""):
    """read filename with utf-8 encoding"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
