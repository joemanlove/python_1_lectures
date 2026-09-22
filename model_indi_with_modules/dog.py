from random import choice

class Dog:
    def __init__(self, name):
        self.name = name
        self.balls = []

    def action(self, locations, humans):
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
                f'{self.name} has found the {target_ball.name} in the {target_location.name}.')
        else:
            print(
                f'{self.name} looks hopelessly about after searching the {target_location.name}.')
