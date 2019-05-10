#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    multiplied = list(map(lambda factor: factor * number, my_list))
    return multiplied
