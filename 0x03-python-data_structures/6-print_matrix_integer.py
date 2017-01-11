#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        print("{}".format(" ".join(str(n) for n in sublist)))
