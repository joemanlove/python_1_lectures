"""
Making Your Own Modules Lecture written by Joe Manlove

Revised on 9/28/2020
Revised on 9/22/2026 to include docstrings.
"""

# Some definitions, most of these are a little loose
# a single python file intended to be executed individually is a 'script'
# you'll have heard me say 'sketch' or 'program' instead of script a few times, those are artifacts from other languages

# a module is a python file intended to be imported into a script
# they usually do not have a script functionality, but may

# a package is an organized set of modules

# a library usually refers to a published package, although it may be a module
# libraries are almost never executable

# Import the randint function from the random library
# this is needed for line 30, but is not available to the test_module
from random import randint

# import the two functions from the test_module
from test_module import double, random_multiply

# this executes only if this file is run
if __name__ == "__main__":
    print('primary script...')
    print(randint(1, 10))

# testing out our functions from the module
print(f"Double 6 is {double(6)}")
print(f"Random_multiply of 6 is {random_multiply(6)}")
