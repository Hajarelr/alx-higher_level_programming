#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []
    for line in matrix:
        s.append([c**2 for c in line])
    return s
