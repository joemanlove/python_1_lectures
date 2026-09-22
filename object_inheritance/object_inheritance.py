"""
Object Inheritance Lecture written by Joe Manlove

Based on the Model Indi assignment code from earlier in the Python 1. That code is in the model_indi folder in this github repo.
This version revised to include class inheritance on 6/5/2020.
Revised to include docstings and fix naming conventions 9/22/2026.

Further revisions to refactor this code into modules can be found in the folder model_indi_with_modules in this github repo.
Further revisions to this code to add more extensive docstrings can be found in the docstrings_and_modules folder in this github repo.
"""

# Pet class
class Pet:
  def __init__(self, name, weight, color):
    self.name = name
    self.weight = weight
    self.color = color

  def say_hi(self, greeting):
    print(f'{greeting} My name is {self.name}, I weigh {self.weight} pounds and I\'m {self.color}.')


# Cat class extends the Pet class
class Cat(Pet):
  def __init__(self, name, weight, color, inside, declawed):
    super().__init__(name, weight, color)
    self.inside = inside
    self.declawed = declawed

  def say_hi(self):
    #print(f'Row, Mau! My name is {self.name}, I weigh {self.weight} pounds and I\'m {self.color}.')
    greeting = 'Row, Mau!'
    super().say_hi(greeting)
    if self.inside:
        print('I live in the house.')
    if self.declawed:
        print('My claws were pulled, because hoomans are mean.')


# Dog class extends the Pet class
class Dog(Pet):
  def __init__(self, name, weight, color):
    super().__init__(name,weight,color)
    self.collar = True

  def say_hi(self):
    #print(f'Bork, bork! My name is {self.name}, I weigh {self.weight} pounds and I\'m {self.color}.')
    greeting = 'Bork, bork!'
    super().say_hi(greeting)

  def swim(self):
    print(f'{self.name} is swimmin\'.')


indi = Dog('Indi', 68, 'Blue Merel')
indi.say_hi()
indi.swim()

rumor = Cat('Rumor', 12, 'Tabby', True, False)
rumor.say_hi()

blue = Dog('Blue', 25, 'Blue Meral')
blue.say_hi()

print(type(rumor))
print(isinstance(10, object))