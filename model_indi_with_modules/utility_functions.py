def balls_to_string(balls):
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
