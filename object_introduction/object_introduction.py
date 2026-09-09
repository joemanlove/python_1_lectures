"""
Object Introduction Lecture by Joe Manlove

revised on 5/24/20
revised on 9/8/26 to fix comments, naming, and add docstrings.
"""

# define the Dog class
class Dog:
    """
    The dog class represents the abstract idea of a dog.
    
    Attributes:
        name (str): The name of the dog.
        weight (int): The weight of the dog in pounds.
        color (str): The dog's color.

    """
    # initialize method
    def __init__(self, name: str, weight: int, color: str):
        
        # set the dog's name
        self.name = name
        # set the dog's weight
        self.weight = weight
        # set the dog's color
        self.color = color
    
    # The say_hi method is for diagnostic purposes.
    def say_hi(self):
        print(f"I'm {self.name}. I weigh {self.weight} pounds, and my coat is {self.color}.")


# Create instances. Instances of a class are also called objects.
indi = Dog('Indi', 68, 'blue merle')
blue = Dog('Blue', 28, 'black and brown')

# Call the say_hi method on both instances.
indi.say_hi()
blue.say_hi()