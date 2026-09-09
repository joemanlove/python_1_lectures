"""
Object Example - Kombucha Recipe by Joe Manlove

The recipe here is courtesy of Lahna VonEpps.
Revised on 8/8/26 to fix docstrings, naming, and update error handling. 
"""

# Import the ceiling function from the math library.
from math import ceil


# define a Kombucha class (probably a bit overkill)
class Kombucha():
    """
    A kombucha object represents the abstract concept of a batch of kombucha.

    Attributes:
        water_cups (int): The number of cups of water needed for the batch.
        sugar_cups (int): The number of cups of sugar needed for the batch.
        teabags (int): The number of teabags needed for the batch.
    """

    def __init__(self):
        # properties:
        # cups of water
        self.water_cups = 0
        # cups of sugar (1 for every 4 of water)
        self.sugar_cups = 0
        # number of teabags (1 teabag for every 3 cups of water)
        self.teabags = 0

    # methods
    # desired amount in gallons to recipe amounts
    def gallons_to_kombucha(self, gallons:int):
        """
        Sets (or resets) all the attributes of a batch based on the amount of kombucha desired.

        Args:
            gallons (int): The number of gallons of kombucha desired. (Think container size.)
        """
        # There are 16 cups in a gallon.
        # Ceiling rounds up to the nearest integer.
        self.water_cups = ceil(16 * gallons)
        self.sugar_cups = ceil(self.water_cups / 4)
        self.teabags = ceil(self.water_cups / 3)

        # print recipe
    def print_recipe(self):
        print(f'Use {self.water_cups} cups of water.')
        print(f'Use {self.sugar_cups} cups of sugar.')
        print(f'Use {self.teabags} teabags.')


# make a kombucha object
booch = Kombucha()

# loop continuously
while 1 == 1:
    # solicit user input
    userAmt = input('How many gallons of Kombucha do you want to make?\n')
    try:
        amt = float(userAmt)
        booch.gallons_to_kombucha(amt)
        booch.print_recipe()
    except ValueError:
        print('Please enter a numeric value.')
