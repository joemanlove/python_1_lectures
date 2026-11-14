# Sending email from Python
# written by Joe Manlove
# created 11/9/2020
# largely plagiarized from some python2 code and Stack


import smtplib
from configparser import ConfigParser

config = ConfigParser()

# This is what config.ini looks like
# [Gmail]
# user_name = UsarsNamer
# password = PassWerd

config.read('config.ini')
user_name = config['Gmail']['user_name']
password = config['Gmail']['password']

print('##############WARNING################')
print('##############WARNING################')
print('##############WARNING################')
print('##############WARNING################')
print('DO NOT PUT YOUR GMAIL CREDENTIALS INTO A REPL')
print('DO NOT COMMIT YOUR GMAIL CREDENTIALS TO GIT')
print('DO GO ON AND HAVE AN EXCELLENT ENJOYABLE DAY')
print('##############WARNING################')
print('##############WARNING################')
print('##############WARNING################')
print('##############WARNING################')

def send_email(user, pwd, recipients, subject, body):
    """
    Sends an email from a gmail account. Gmail account must have 'allow less secure apps' enabled.

    Arguments:
        user, a string gmail username
        pwd, a string - the user's password
        recipients, a list of strings - recipient emails
        subject, a string
        body, a string
    Returns:
        None
    """

    # to allow less secure apps: https://www.google.com/settings/security/lesssecureapps
    message = f'From: {user}\nTo: {", ".join(recipients)}\nSubject: {subject}\n\n{body}'

    # making a SMTP object
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # say ehlo to the main gmail servers from our system
    server.ehlo()
    # establish secure connection
    server.starttls()
    
    server.login(user, pwd)
    server.sendmail(user, recipients, message)
    server.close()
    print('Successfully sent the mail.')

# This line would send an email...
# send_email(user_name, password, ['person@place.com'], 'TEsting the EMAILER!!', 'Some texting text...')
