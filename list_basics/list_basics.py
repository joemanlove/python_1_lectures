"""
List Basics lecture written by Joe Manlove

This should serve as an introduction to lists.
revised 5/19/2020 to include f strings
revised 8/27/2026 to fix naming conventions, make comments more readable, and add this docstring.
"""

# What's a list?
# A list is a container for multiple pieces of information.
# They are ordered (numbered) starting with 0.
# The number associated to a particular slot is called the "index".
# Lists are variable in size as opposed to arrays. Arrays are not really a thing in standard Python.
# Be careful, Python lists will allow you to store multiple different types of things in the same list.

# How do you make one?
# [0, 1, 2, 3, 4]
numbers = [1,2,3,5,6,7,7,7]

# Use the copy method to copy a list, if you don't you'll just have two names for the same list.
old_numbers = numbers.copy()

# Printing the list out.
print(numbers)

# Operations with Lists?
# Use append to add an item to the end of the list.
numbers.append(10)
# Print the updated list out.
print(f'The new list is now {numbers}.')

# Use insert to add an item in a specific slot.
numbers.insert(1,'bill')
# Print the updated list out.
print(f'The new list is now {numbers}.')

# Remove the first occurrence of 'bill'.
numbers.remove('bill')
# Print the updated list out.
print(f'The new list is now {numbers}.')
# The function "len" (short for "length") tells us how many items are in the list.
print(f'The numbers list has {len(numbers)} things in it.')

# The function "pop" removes and returns the value at the specified index.
# If you don't call pop on a specific number, it will remove and return the last entry.
numbers.pop(0)
# Print the updated list out.
print(f'The new list is now {numbers}.')

# Print out the length of the updated list.
print(f'The numbers list has {len(numbers)} things in it.')
# Use clear to erase all the items.
numbers.clear()
# Print the updated list out.
print(f'The new list is now {numbers}.')

# Print out the length of the updated list.
print(f'The numbers list has {len(numbers)} things in it.')

# Print the old list out.
print(f'The old list is {old_numbers}.')

# It might be enlightening to go back to 
# old_numbers = numbers.copy()
# and change it to
# old_numbers = numbers
# to see the difference.