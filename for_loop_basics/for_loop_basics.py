"""
Lecture on the basics of for loops written by Joe Manlove

Revised on 5/23/20.
Revised 8/27/2026 to add this docstring and clean up comments.
"""

# Below are some example variables and lists to consider.
# This list is the names of some of my pets.
pets =  ['Indigo', 'Blue', 'Rumor']

# My friend John used to tell people that his job as a mathematician consisted of trying to find a new number.
# He called it 'spevdo' and used to say he was pretty sure it was between 6 and 7.
spevdo = 'Spevdo'

# This variable is just the number 37 which is nice.
number = 37

# This is a way to loop through the pets list and print each item. This is my preferred method.
for pet in pets:
  print(pet)

# This is an alternate method to loop through the pets list and print each item.
print('Alternative method of looping:')
for i in range(len(pets)):
  print(pets[i])


# This is a way to loop through the letters of 'Spevdo'. This works because both strings and lists are iterables.
for letter in spevdo:
  print(letter)

# This is how you loop a set number of times.
# The variable i will go from 0 to number - 1.
for i in range(number):
  print(i)

# You can enumerate a list, i will be the index and pet will be the value. This is an example of a thing called unpacking.
for i, pet in enumerate(pets):
  print(i, pet)