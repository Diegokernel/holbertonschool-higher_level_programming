#!/usr/bin/python3
"""
matrix_divided - divids list of lists
"""

def matrix_divided(matrix, div):
    """
    Return new_matrix with all int in matrix divided by parameter div
    """
	new_matrix = []
	if div == 0:
        	raise ZeroDivisionError("division by zero")
	if type(div) != int and type(div) != float:
        	raise TypeError("div must be a number")
	for row in matrix:
    	if len(matrix[0]) != len(row):
        	raise TypeError("Each row of the matrix must have the same size")
	for row in matrix:
    	if all(isinstance(x, (int, float)) for x in row) is False:
        	raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
 	if not all(isinstance(row, (list)) for row in matrix):
        	raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
 	for i in matrix:
        	new_matrix.append(list(map(lambda x: round(x/div, 2), i)))
   	return new_matrix
