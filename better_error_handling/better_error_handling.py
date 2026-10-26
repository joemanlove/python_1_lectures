"""
Better Error Handling Lecture written by Joe Manlove

created 7/20/2020
revised 10/20/2026 to add this docstring and fix some spelling errors
"""

# try block always gets attempted
# try to typecast the user input into an integer
try:
    # get user input
    answer = input('Please provide an integer...\n')

    # reply to user their answer
    print(f'You said {answer}. \nProcessing, please wait...')

    number = int(answer)
    # print out result
    print(f'You said {number}. This is of type: {type(number)}')

# except blocks will execute on errors
except ValueError:
    print('I\'m afraid that\'s not a number, Dave.')

except BaseException as error:
    print('Quitter....    :(')
    raise error


# else block is executed if the try block succeeds.
else:
    print('This is the else block.')

# finally block always get executed regardless
finally:
    print('This is the finally block.')