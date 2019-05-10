#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        val = a_dictionary[key]
        if val is value:
            del val
        return a_dictionary
