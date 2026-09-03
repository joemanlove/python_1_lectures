"""
While loops lecture

Written by Joe Manlove
Inspired by my small niece's request for bananna
Last revision 5/24/20
"""

answer = ''

while answer != 'yes':
  answer = input('Nana?\n')
  if answer.lower() == 'go to sleep.':
    print('Cry...')
    break
  elif answer == 'yes':
    print('Yumm... Happy chewing...')

print('This has been a conversation with Ailish.')