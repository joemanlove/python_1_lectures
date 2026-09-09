"""
Model Indi Assignment Template by Joe Manlove

Revised on 5/31/20
Revised on 9/8/26 to include docstring and fix naming.
The assignment is to add comments and docstrings to this.
"""


from random import choice

locations = []
humans = []
dogs = []


def ball_string(balls):
    if len(balls) == 0:
        return 'no balls'
    elif len(balls) == 1:
        return f'{balls[0].name}'
    elif len(balls) == 2:
        return f'{balls[0].name} and {balls[1].name}'
    else:
        return_string = ''
        for ball in balls[:-1]:
            return_string += ball.name + ', '
        return_string += f'and {balls[-1].name}'
        return return_string


class Human:
    def __init__(self, name):
        self.balls = []
        self.name = name

    def action(self):
        if self.balls != []:
            print(f'\nYou now have {ball_string(self.balls)} in your hands...')
            action = input('Throw the ball?\n')
            if action.lower() in ['yes', 'y']:
                self.throw_ball(choice(self.balls), choice(locations))
            else:
                print('You really are heartless aren\'t you?')

    def throw_ball(self, ball, target_location):
        target_location.balls.append(ball)
        self.balls.remove(ball)
        print(
            f'You have thrown {ball.name}, it is now in the {target_location.name}.\n'
        )


class Location:
    def __init__(self, name, balls):
        self.name = name
        self.balls = balls


class Ball:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name):
        self.name = name
        self.balls = []

    def action(self):
        if self.balls != []:
            self.give_ball(choice(humans), choice(self.balls))
        else:
            self.look_for_ball(choice(locations))

    def give_ball(self, human, ball):
        self.balls.remove(ball)
        human.balls.append(ball)
        print(f'{self.name} has given the {ball.name} to {human.name}')

    def look_for_ball(self, target_location):
        if target_location.balls != []:
            target_ball = choice(target_location.balls)
            self.balls.append(target_ball)
            target_location.balls.remove(target_ball)
            print(
                f'{self.name} has found the {target_ball.name} in the {target_location.name}.'
            )
        else:
            print(
                f'{self.name} looks hopelessly about after searching the {target_location.name}.'
            )


locations = [
    Location('Living Room', [Ball('Pink Torus')]),
    Location(
        'Kitchen',
        [Ball('Sal the Snake'),
         Ball('Pink Ellipsoid'),
         Ball('Blue Chuckit')]),
    Location('Under the Couch',
             [Ball('Pink Ball'),
              Ball('Green Ellipsoid'),
              Ball('Blue Torus')]),
    Location('Dining Room', []),
    Location(
        'Yard',
        [Ball('Larry the Lizard'), Ball('S toy')])
]
Joe = Human('Joe')
humans.append(Joe)
Indi = Dog('Indi')
dogs.append(Indi)

while True:
    Indi.action()
    Joe.action()
