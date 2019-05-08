#!/usr/bin/python3
def multiple_returns(sentence):
    longitud = len(sentence)
    if longitud == 0:
        caracter = None
    else:
        caracter = sentence[0]
    return longitud, caracter
