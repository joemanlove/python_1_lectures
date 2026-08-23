"""
This is the code associated to a lecture on variables and types.

It was originally written in 2020. It was updated to include this docstring and fix some small typos in 2026.
"""

# numeric variables include
# integer type - int
# declaration and initialization
x = 10

# there is a difference here:
# in this first one 'x' is a text variable (well, not really a variable, it's actually constant)
print('x')
# in this case, x is a variable's name
print(x)

# float type - float
y = 9.2012
# print 'y' and y
# there are better ways to do this, but it's fast...
# see lecture on string formatting
print('y' , y)

# complex type exists, j instead of i


# text variables are strings - str
# google escape characters for more info
s = 'I\'m stuck in this computer. Help! \\'
print(s)

# sequences
# lists
x = [10,2,3]
print(x)
# more on this later
# array in other languages (ish)

# also: maps, bool, set, binary

# we can check what kind of thing a variable is
print(type(y))
print(isinstance(y, (int,float)))