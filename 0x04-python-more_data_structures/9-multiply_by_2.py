#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    by_2 = {key: a_dictionary[key] * 2 for key in a_dictionary.keys()}
    return by_2
