"""
Decorators lecture written by Joe Manlove

created 7/16/2020
revised 7/18/2020 to explain all the print statements
revised 10/14/2026 to this docstring, other function docstrings are excluded for simplicity.

This code is meant to supplement https://youtu.be/ryNNQZTR39s
Most of the comments are explicitly printed to make the output easier to track
"""

# Prelims
# Functions can be aliased (called by a different name).
print('Functions can be aliased.')

# define an example_function
def example_function():
    print('This is the example_function.')

print('\tCalling the example_function.')
example_function()

ex_fct = example_function

print('\tCalling the ex_fct.')
ex_fct()

# Functions can be defined inside of Functions
print('\nFunctions can be defined inside of functions.')

def outer_function():
    def inner_function():
        print('This is the inner_function.')

    print('This is the outer_function.')
    inner_function()

print('\tCalling the outer_function.')
outer_function()

# Functions can return Functions
print('\nFunctions can return functions.')

# define a greeting_maker function
def greeting_maker(text):
    print('Running the greeting_maker...')
    def greeting():
        print(text + ', to the class.')

    return greeting

print('\tMaking the greeting functions.')
german_greeting = greeting_maker('Vilkommen')
english_greeting = greeting_maker('Welcome')

print('\tCalling the greeting functions.')
german_greeting()
english_greeting()


# Main Idea
# Now for the understandable wrapper    
print('\nUnderstandable wrapper:')

# this is the decorator
def add_wrapper(passed_function):
    def wrapped_function(*args,**kwargs):
        print(f'Running, the {passed_function.__name__}...')
        result = passed_function(*args,**kwargs)
        print('Done.')
        return result
    
    return wrapped_function

def function():
    print('Sup?')

print('\tRunning the function without the wrapper.')
function()

print('\tWrapping the funcion.')
function = add_wrapper(function)

print('\tRunning the wrapped function.')
function()

# Now for the 'decorator' aka, the wrapper syntax people actually use:  
print('Decorator Style:')

print('\tDefining function with decorator.')

@add_wrapper
def decorated_function(number):
    print('This is decorated.', number)

print('\tRunning decorated_function.')
decorated_function(9)

# Adding to existing functions and dealing with returns:
print('\nAdding to existing functions:')

from random import randint

print('\tWrapping the randint function.')
randint = add_wrapper(randint)

print('\tRunning randint.')
print(randint(1,3))