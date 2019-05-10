#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    tmp = 0
    prevnum = 0
    for c in roman_string:
        tmp = rom_dic.get(c, 0)
        if tmp > prevnum:
            num -= 2 * prevnum
            num += tmp
        else:
            num += tmp
            prevnum = tmp
            return num
