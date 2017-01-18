def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" \
                        " of integers/floats")
    if len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists)" \
                        " of integers/floats")
    if not all(len(l) > 0 for l in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" \
                        " of integers/floats")

    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for l in matrix:
        if not isinstance(l, list):
            raise TypeError("matrix must be a matrix (list of lists)" \
                            " of integers/floats")
        if not all(isinstance(x, (int, float)) for x in l):
            raise TypeError("matrix must be a matrix (list of lists)" \
                            " of integers/floats")

    if div is 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for l in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), l)))

    return new_matrix
