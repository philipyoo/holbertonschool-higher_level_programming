def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda n: n**2, sublist)) for sublist in matrix]
    return new_matrix
