#!/usr/bin/python3
"""def append_write functions"""


def append_write(filename="", text=""):
    """append filename at the eof with utf-8 encoding"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
