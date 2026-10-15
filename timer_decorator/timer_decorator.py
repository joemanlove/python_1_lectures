"""
Timer Decorator Lecture written by Joe Manlove

Created 7/17/2020
Revised 7/18/2020 after video to fix spelling of Fibonacci and add comments.
Revised 10/14/2026 to add docstrings and update comments about decorating recursive functions.
"""

from time import time, sleep
from fibonacci import fibonacci


def with_timer(function):
    """ Adds a timer to a function, in seconds. """

    def function_with_timer(*args, **kwargs):
        # stores the start time
        start = time()
        # stores the function output for later return
        value = function(*args, **kwargs)
        # stores the end time, duration is end - start
        end = time()

        # Output the timer information, function.__name__ can be
        #   a bit problematic when combined with multiple decorators
        print(f'{function.__name__} took {end-start} seconds to execute.')

        # return the original function output so the decorated function and the
        #   original have the same output
        return value

    # return the idea of the decorated function
    return function_with_timer

# declare a test function with the with_timer decorator
@with_timer
def test_function():
    """Sleeps for two seconds. Should take two seconds to run."""
    sleep(2)

test_function()

# For an imported function this syntax will work.
# If the imported function is recursively defined it will only wrap the outermost layer.
# That's what we'd like in the case of a timer, but can be an issue with memoization.
# See the memoization lesson for more details.
fibonacci = with_timer(fibonacci)

# another test, expect this to take between 5 and 20 seconds.
fibonacci(40)
