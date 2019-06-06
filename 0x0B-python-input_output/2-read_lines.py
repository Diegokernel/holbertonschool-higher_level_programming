#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="utf-8") as filer:
        if not nb_lines <= 0:
            for i in range(nb_lines):
                print(filer.readline(), end="")
            else:
                read_f = filer.read()
                print(read_f, end='')
