#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def my_add():
        total = add(num1, num2)
        print("{:d} + {:d} = {:d}".format(num1, num2, total))
        return total

    def my_sub():
        total = sub(num1, num2)
        print("{:d} - {:d} = {:d}".format(num1, num2, total))
        return total

    def my_mul():
        total = mul(num1, num2)
        print("{:d} * {:d} = {:d}".format(num1, num2, total))
        return total

    def my_div():
        total = div(num1, num2)
        print("{:d} / {:d} = {:d}".format(num1, num2, total))
        return total

    options = {
        "+": my_add,
        "-": my_sub,
        "*": my_mul,
        "/": my_div
    }
    options.get(op, not_found)()
