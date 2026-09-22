from utility_functions import balls_to_string
from random import choice

class Human:
    def __init__(self, name):
        self.balls = []
        self.name = name

    def action(self, locations):
        if self.balls != []:
            print(
                f'\nYou now have {balls_to_string(self.balls)} in your hands...')
            action = input('Throw the ball?\n')
            if action.lower() in ['yes', 'y']:
                self.throw_ball(choice(self.balls), choice(locations))
            else:
                print('You really are heartless aren\'t you?')

    def throw_ball(self, ball, target_location):
        target_location.balls.append(ball)
        self.balls.remove(ball)
        print(
            f'You have thrown {ball.name}, it is now in the {target_location.name}.\n')
