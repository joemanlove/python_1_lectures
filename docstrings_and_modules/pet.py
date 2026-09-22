"""Provides the Pet, Dog, and Cat classes."""

# Pet class
class Pet:
  """ Pet class represents a household Pet.

  Contains name, weight, color attributes, and a SayHi method. Specific extensions should be based off this class. This is intended only to be a base class.
  """
  def __init__(self, name, weight, color):
      self.name = name
      self.weight = weight
      self.color = color

  def sayHi(self, greeting):
      print(f'{greeting} My name is {self.name}, I weigh {self.weight} pounds and I\'m {self.color}.')

# Cat class extends the Pet class
class Cat(Pet):
  """ The Cat class extends the Pet class.

  Extends Pet attributes by inside and declawed booleans. Also provides an enhanced sayHi method.
  """
  def __init__(self, name, weight, color, inside, declawed):
    """ Initialize an instance of Cat class.

    name -- name as a string,
    weight -- in pounds,
    color -- color as string
    """
    super().__init__(name,weight,color)
    self.inside = inside
    self.declawed = declawed

  def sayHi(self):
      """ Print a customized greeting. """
      greeting = 'Row, Mau!'
      super().sayHi(greeting)
      if self.inside:
          print('I live in the house.')
      if self.declawed:
          print('My claws were pulled, becuase hoomans are mean.')
    
# Dog class extends the Pet class
class Dog(Pet):
  """ The Dog class extends the Pet class.

  Extends Pet attributes by collar boolean. (Always defaults to True.) Also provides an enhanced sayHi method. Provides a swim method.
  """ 
  def __init__(self, name, weight, color, collar = True):
      super().__init__(name,weight,color)
      self.collar = collar

  def sayHi(self):
      """ Print a customized greeting. """
      greeting = 'Bork, bork!'
      super().sayHi(greeting)

  def swim(self):
      """ Narrate swimming. """
      print(f'{self.name} is swimmin\'.')
