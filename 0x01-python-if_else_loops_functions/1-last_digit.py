#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if (ldigit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, ldigit))
elif (ldigit == 0):
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, ldigit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, ldigit))
