#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        print(' '.join(["{:d}".format(elem) for elem in fila]))
