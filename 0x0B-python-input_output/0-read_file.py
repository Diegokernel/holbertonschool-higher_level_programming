#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as filer:
        print(filer.read(), end='')
