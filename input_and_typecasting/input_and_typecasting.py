"""
This is the code associated to a lecture on input and typecasting.

This code was created in 2020 to illustrate collecting input from a user and the issues that often arise from doing so.
It was modified in 2026 to include this docstring and adhere to naming conventions.
The secondary goal of this script is to collect information on the population of eels in the user's hovercraft.
"""

# ask the user how many eels are in their hovercraft, store result in user_said_what variable
user_said_what = input('How many eels are in your hovercraft?\n')

# for debugging
# print(type(user_said_what))

# force user_said_what into an integer, store that in num_eels
num_eels = int(user_said_what)

# this is an example of formatting strings
print(f'So, there are {2*num_eels} eel eyes in your hovercraft.')

# string concatenation method
print('Number of eels: ' + str(num_eels))