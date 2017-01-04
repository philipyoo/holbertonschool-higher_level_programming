# 0x01. Python - if/else, loops, functions

This directory contains exercises/projects for learning about Python if/else statements, loops, and building functions.

| File | Description |
| ---- |:-----------:|
| 0-positive_or_negative.py | Given a random number, print to stdout is the singles digit is positive, zero, or negative. |
| 1-last_digit.py | Given a random number between -10,000 to 10,000, print to stdout if the singles digit is greater than 5, equal to 0, or less than 6 and not 0. |
| 2-print_alphabet.py | Print to stdout the alphabet with no newline. Restricted to using only one `print` function, one loop, and cannot import any modules. |
| 3-print_alphabt.py | Print to stdout the alphabet with no newline except for letters "q" and "e". Same restrictions apply to exercise 2. |
| 4-print_hexa.py | Print all numbers from 0 to 98 in decimal and hexadecimal. Restricted to using only one `print` with string format statement, one loop, and cannot import any modules. |
| 5-print_comb2.py | Print to stdout numbers 0 to 99. Numbers must be comma and space separated, should print in ascending order with 2 digits, and the last number should be followed by a newline. Restricted to using no more than 2 `print` functions with string format, one loop, and cannot import any modules. |
| 6-print_comb3.py | Print to stdout all possible different combinations of two digits from 0 to 99. 01 and 10 are considered as the same combination of digits 0 and 1. Must print in ascending order, and tens digit must be lower than singles digit. Numbers must be comma and space separated. Restricted to no more than 3 `print` functions with string format, 2 loops, and cannot import any modules. |
| 7-islower.py | Write a function that checks if a character is lowercased. Return a boolean value. Assume input will always be a single character. Default to printing "upper" for invalid characters. Cannot import any modules, and cannot use `.upper()` and `.isupper()`. |
| 8-uppercase.py | Print to stdout a string in uppercase followed by a newline. Restricted to no more than 2 `print` functions with string format, one loop, cannot import any modules, and cannot use `.upper()` and `.isupper()`. |
| 9-print_last_digit.py | Write a function that prints the last digit of a number. Cannot import any modules. |
| 10-add.py | Write a function that adds two integers and returns the result. Cannot import any modules. |
| 11-pow.py | Write a function that computes `a` to the power of `b` and return the value. Cannot import any modules. |
| 12-fizzbuzz.py | Write a function that prints the numbers from 1 to 100 separated by spaces. For each multiple of 3, print "Fizz". For each multiple of 5, print "Buzz". For each multiple of both 3 and 5, print "FizzBuzz". Cannot import any modules. |
| 100-print_tebahpla.py | Write a program that prints the alphabet, in reverse order, alternating lowercase and uppercase starting with lowercase "z", not followed by a newline. Restricted to only one `print` function with string format, one loop, and cannot import any modules. |
| 101-remove_char_at.py | Write a function that creates a copy of the string, removing the character at position `n`. Cannot import any modules. |
| 102-magic_calculation.py | Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the Python bytecode given. See below for more info. |


## Other

For exercise 102, we are given a Python bytecode. We are tasked with writing a function that disassembles exactly into the bytecode we are provided. The bytecode we were given was:

```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```