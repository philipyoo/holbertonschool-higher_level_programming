#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv)
    total = 0
    for i in range(1, num_args):
        total += int(argv[i])
    print("{:d}".format(total))
