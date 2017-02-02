#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            count += 1
    return count
