#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        maxi = my_list[-1]
        return maxi
    else:
        return None
