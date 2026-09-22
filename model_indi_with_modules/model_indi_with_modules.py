"""
Model Indi Assignment Template Refactored into Modules written by Joe Manlove

Created 5/31/20
Revised 9/28/2020 to bring to PEP8 naming standards and utilize modules
Revised 9/22/2026 to add this docstring.

Note, this file is used as an assignment earlier in the course to add comments to, so it remains uncommented.
For a commented version with proper docstrings refer to docstrings_and_modules in this github repo.
"""

from location import Location
from ball import Ball
from human import Human
from dog import Dog


locations = []
humans = []
dogs = []

locations = [
    Location('Living Room', [Ball('Pink Torus')]),
    Location('Kitchen', [Ball('Sal the Snake'), Ball('Pink Ellipsoid'), Ball('Blue Chuckit')]),
    Location('Under the Couch', [Ball('Pink Ball'), Ball('Green Ellipsoid'), Ball('Blue Torus')]),
    Location('Dining Room', []),
    Location('Yard', [Ball('Larry the Lizard'), Ball('Hook Dongle')])
    ]


joe = Human('Joe')
humans.append(joe)
indi = Dog('Indi')
dogs.append(indi)

while True:
    indi.action(locations, humans)
    joe.action(locations)
