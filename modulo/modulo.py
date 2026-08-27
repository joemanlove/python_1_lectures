"""
Modulo written by Joe Manlove

lecture on the division algorithm, integer division, and the modulo operator
revised 5/19/2020 to add f strings
revised 8/27/2026 to add this docstring, fix naming conventions, and make comments more readable.
"""

# The guiding principle for this lecture follows:
# Computers are good at calculating, but humans are bad at numbers, good programs can bridge the gap.

# We'll find ourselves in need of some randomness so we'll import the randint function from the random library.
from random import randint

# Get a random number of hours.
num_hours = randint(-180,180)
print(f'Starting with {num_hours} hours...')

# Find out how many days by dividing by 24.
num_days = num_hours//24

# Find out how many leftover hours there are.
left_over_hours = num_hours%24

# Print out the results.
print(f"That's {num_days} days and {left_over_hours} hours.")

# Print out the results reversing the calculation for error checking.
print(f'The original number of hours was {num_days * 24 + left_over_hours}.')
