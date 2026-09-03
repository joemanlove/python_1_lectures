"""
Conditionals, Logic, and Tests

Written by Joe Manlove
Revised 5/23/20
Revised 8/29/26 to fix some naming, comments, and docstrings.
"""


# This is an example function for use below.
def send_cookie():
  """Sends the user a cookie via email."""
  # TODO make this function email the user a cookie
  print('Sending cookie...')

# Remember booleans are either True or False.
# First we look at the syntax for if, elif, and else.

# Ask the user if they'd like a cookie, store their input into the "answer" variable.
answer = input('Would you like a cookie?\n')

# A word of caution, 'C' is always True, so the following will always print "Yum...".
# if answer == 'YUM' or 'C':
#   print('Yum...')

# lower converts to lowercase
if answer.lower() == 'yes' or answer.lower() == 'y':
  send_cookie()

# else if answer is roughly no
elif answer.lower() == 'no' or answer.lower() == 'n':
  print('too bad...')

# otherwise
else:
  print('Wut?')


# Ask the user their name.
answer = input('What\'s your name?\n')

# Steve and Bill are VIP members so they get super enthusiastic greetings, everyone else gets standard greetings.
# This is my preferred method for checking user input against a list of possible answers.
if answer in ['Steve','Bill']:
  print('Hey!')
else:
  print('hi')


