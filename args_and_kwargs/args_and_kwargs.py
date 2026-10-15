"""
Using *args and **kwargs Lecture written by Joe Manlove

created 7/15/2020
revised 10/14/2026 to add docstrings
"""

# * is the 'unpacking operator'

def sum(*args):
    """
    Define a function to add up any number of arguments.
    This definition is saying 'expect an unpacked tuple *args' so args is a tuple made out of everything that got passed.

    Args:
        *args: an unpacked tuple
    """
    result = 0
    # args is the packed version of all the arguments
    # go through it one at a time, adding to results
    for argument in args:
        result += argument
    return result

# print a test call of sum
print(sum(1,5,4,23,7,8,9))

# testing some unpackng with tuples
test_tuple = (1,2,3)
print(test_tuple)
print(*test_tuple)


def dictionary_dump(**kwargs):
    """Example function that accepts an unpacked dictionary."""

    # kwargs is the packed dictionary
    # print out the packed dictionary
    print(kwargs)

    # loop through all items in kwargs print associations
    for key, value in kwargs.items():
        print(f'{key} is associated to {value}')

# test call of the dictionary dump function
dictionary_dump(a = 'apple', b = 'bear')
