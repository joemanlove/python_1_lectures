"""Test Module with double and random_multiply functions."""

# import the randint function from the random library for use in this module
from random import randint

# this will not run unless this file is executed. Repl won't execute it so far as I know.
if __name__ == "__main__":
    print("This is the test_module....")

# doubling function to test
def double(x: float) -> float:
    """Returns double the value of a parameter."""
    return 2 * x

# random multiple function to test
def random_multiply(x):
    """Returns a random multiple of the supplied parameter. Possible multiples are integers between 1 and 10 inclusive."""
    return randint(1,10)*x
