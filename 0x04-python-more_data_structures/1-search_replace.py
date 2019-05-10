#!/usr/bin/python3
def search_replace(my_list, search, replace):
        change_list = [replace if elem is search else elem for elem in my_list]
        return change_list
