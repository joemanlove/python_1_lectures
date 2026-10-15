"""
Decorators written by Joe Manlove

created 7/17/2020 - included with_timer
"""

from time import time
from functools import wraps

def with_timer(function):
    """ Adds a timer to a function, in seconds.
    Preserves arguments and returns.
    """

    # using the wraps decorator keeps docstrings and name attributes
    @wraps(function)
    def function_with_timer(*args, **kwargs):
        start = time()
        value = function(*args, **kwargs)
        end = time()

        print(f'{function.__name__} took {end-start} seconds to execute.')

        return value

    return function_with_timer
