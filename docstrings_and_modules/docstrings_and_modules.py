"""
Docstrings and Modules - revision of Object Inheritance Lecture based on Model Indi written by Joe Manlove

This version revised 6/6/2020 from model_indi and object_inheritance in this github repo.
See also model_indi_with_modules for a more modular version of this code.

Docstrings Python Enhancement Proposal: https://www.python.org/dev/peps/pep-0257/

This version revised 9/22/2026 to include this docstring and a docstring for the pet module.
"""
  

from pet import Dog, Cat

indi = Dog('Indi', 68, 'Blue Merel')
indi.sayHi()
indi.swim()

rumor = Cat('Rumor', 12, 'Tabby', True, False)
rumor.sayHi()

blue = Dog('Blue', 25, 'Blue Meral')
blue.sayHi()

# print(type(rumor))
print(isinstance(10, object))