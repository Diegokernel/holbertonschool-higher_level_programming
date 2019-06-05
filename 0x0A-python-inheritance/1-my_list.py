#!/usr/bin/python3
''' class MyList that inherits from list'''
class MyList(list):
    ''' prints a list in sorted order '''
    def print_sorted(self):
        print(sorted(self))
