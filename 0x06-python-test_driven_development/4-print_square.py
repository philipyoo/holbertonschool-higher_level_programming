def print_square(size):
    try:
        if not isinstance(size, (int, float)):
            raise TypeError("size must be an integer")
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        for i in range(int(size)):
            print("#" * size)

    except Exception as err:
        print(err)
