"""
Mutable vs Immutable Types Lecture by Joe Manlove

Revised on 5/25/20
Revised on 9/8/26 to clean up naming and docstrings.

Sharpen your brain, we've made this can of worms, now it's time to lie in it.
Seriously tho, this gets a little subtle, pay close attention.

Sourcing:
    https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/
    https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
    especially the comment by Marc Grossouvre, see text file for an archived version.

First, every variable is an instance of an object.
In statically typed languages people often talk about 'passing by reference' or 'passing by value'
Python only passes by reference. It just fakes as passing by value sometimes.
"""

# Immutable Types: "These are of in-built types like int, float, bool, string, unicode, tuple. In simple words, an immutable object can't be changed after it is created."

x = 10
y = x

# print(type(x))

# print(id(x))
# print(id(y))

# y += 1
# print(id(y))

player_list = ['ZedTux', 'FinancedWaif7']

print(id(player_list))

player_list += ['Rando']

print(id(player_list))

print(player_list)

# creates a new storage location
# list = list + [new thing]

# add to memory location that exists
# list += [newthing]
# list.append(newthing)

def addRobert(pL):
    pL = pL + ['PrettyRobert']
    pL.append('PrettyRobert100')
    
    print(pL)

addRobert(player_list)

print(player_list)