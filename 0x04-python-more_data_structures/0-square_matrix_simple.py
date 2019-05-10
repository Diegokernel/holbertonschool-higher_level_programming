#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_elem = [[elem * elem for elem in fila] for fila in matrix]
    return square_elem
