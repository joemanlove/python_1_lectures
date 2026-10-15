"""
Memoization with Import written by Joe Manlove

Created 7/17/2020
Revised 7/18/2020 after video to include lru_cache and alternatives for imported functions. 
    see https://stackoverflow.com/questions/62962678/memoization-of-imported-functions-in-python
Revised 11/17/2020 to add @wraps from the functools library
Revised 10/14/2026 to add docstring and 
"""

from decorators import with_timer
from functools import wraps


def with_memoization(function):
    """
    Add Memoization to a function. Preserves arguments and returns.
    Note, there is an issue with adding memoization to imported recursive functions.
    Imported functions must be memoized by using
        import module
        module.function = with_memoization(module.function)
    Because it is fundamentally an alias, the following is ineffective
        from module import function
        function = with_memoization(function)
    """
    past_results = {}

    # using the wraps decorator keeps docstrings and name attributes
    @wraps(function)
    def function_with_memoization(*args, **kwargs):
        if args not in past_results:
            past_results[args] = function(*args, **kwargs)
        return past_results[args]
    return function_with_memoization


# Memoization for a function defined within the file
@with_memoization
# the decorator @lru_cache(maxsize = 1000) could be used instead of ours
@with_timer
def fib(n):
    """
    the first two cases are 0 -> 0, 1-> 1, otherwise an element is the sum of the previous two
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(100))

# Alternative 1
# Memoization for an imported function using our decorator.
# import fibonacci

# fibonacci.fibonacci = with_memoization(with_timer(fibonacci.fibonacci))

# print(fibonacci.fibonacci(100))


# Alternative 2
# Memoization using the lru_cache decorator from functools module with an imported function
# from functools import lru_cache
# import fibonacci


# fibonacci.fibonacci = lru_cache(maxsize=1000)(with_timer(fibonacci.fibonacci))
# print(fibonacci.fibonacci(100))
