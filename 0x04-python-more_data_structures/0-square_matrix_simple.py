#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix =[[t**2 for t in row] for row in matrix]
    return new_matrix
print(new_matrix)
