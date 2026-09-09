"""
Variable Scope Lecture by Joe Manlove

Revised on 6/4/20
Revised on 9/8/26 to include this docstring and fix one minor naming issue.

Note: Docstrings are omitted in all classes/functions/methods here for clarity. Scope is confusing enough.
"""

# this x is global
x = 1
print(f'At the beginning, global x is {x}.')

# define a function to experiment with
def function():
  # when we use x it'll be the global one
  global x
  x = 4
  print(f'Inside the function, at the beginning, x is {x}.')

  # defines a function inside the function
  def inner_function():
    # this is a new x, that only exists inside the inner function
    x=6
    print(f'Inside the inner function, at the beginning, x is {x}.')

  # call the innerFunction
  inner_function()
  print(f'Inside the function, at the end, x is {x}.')

# a second function for illustrative purpose
def function2():
  print(f'Inside the function2, at the beginning, x is {x}.')
  
# call functions
function()
function2()

# experimental class
class Object:
  def __init__(self):
    self.x = 10
  
  def func(self):
    # global x
    x = 20
    print(f'The variable x is {x}.')
    print(f'The variable self.x is {self.x}.')

# make an instance of the object
obj = Object()

# call the object's function
obj.func()

print(f'At the end, global x is {x}.')