The ``Add Integer`` module
============================

Using ``add_integer``
---------------------

This is an example text file in reStructuredText format. First
``add_integer`` from the ``Add Integer`` module:

	>>> add_integer = __import__("0-add_integer").add_integer

Now use it:

    	>>> add_integer("School", 1)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(1, "School")
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer(float("inf"), 1)
	Traceback (most recent call last):
	    ...
	OverflowError: cannot convert float infinity to integer

	>>> add_integer(1, float("inf"))
	Traceback (most recent call last):
	    ...
	OverflowError: cannot convert float infinity to integer

	>>> add_integer(-float("inf"), 1)
	Traceback (most recent call last):
	    ...
	OverflowError: cannot convert float infinity to integer

	>>> add_integer(1, -float("inf"))
	Traceback (most recent call last):
	    ...
	OverflowError: cannot convert float infinity to integer

	>>> add_integer([1, 2, 3], 0)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(0, [1, 2, 3])
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer({1: "yo"}, 0)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(0, {1: "yo"})
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer(2, 96)
	98

	>>> add_integer(-2, -96)
	-98

	>>> add_integer(100, -2)
	98

	>>> add_integer(-2, 100)
	98

	>>> add_integer("Hello", "Holberton")
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(100.1, -2.9)
	98

	>>> add_integer(True, 2)
	3

	>>> add_integer(2, False)
	2

	>>> add_integer(None, 1)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(1, None)
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer(None, None)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(10.9, 2)
	12

	>>> add_integer(2, 10.9)
	12

	>>> add_integer(-2.9, 10)
	8

	>>> add_integer(2.9, -10)
	-8

	>>> add_integer({1, 2, 3}, 2)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(2, {1, 2, 3})
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer((1, 2, 3), 2)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(2, (1, 2, 3))
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer("17", 2)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(2, "17")
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer([1], [2, 3])
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(lambda x: x, 2.5)
	Traceback (most recent call last):
	    ...
	TypeError: a must be an integer

	>>> add_integer(2.5, lambda x: x)
	Traceback (most recent call last):
	    ...
	TypeError: b must be an integer

	>>> add_integer()
	Traceback (most recent call last):
	    ...
	TypeError: add_integer() missing 2 required positional arguments: 'a' and 'b'

	>>> add_integer(1)
	Traceback (most recent call last):
	    ...
	TypeError: add_integer() missing 1 required positional argument: 'b'
