"""
Translate to PigLatin Example by Joe Manlove

This is an example of taking user input and applying a function to it.

The rules for PigLatin in this example are below, but piglatin is apparently not well defined.
+ if the word starts with a consonant, move the consonant to the end and add 'ay' afterwards i.e. pops -> opspay
+ if the word starts with a vowel, add 'yay' to the end of the word i.e. ouch -> ouchyay
+ this is apparently nonstandard, but the standard version is a bit harder.
+ TODO validate input, maybe check for special characters, multiple words?

Revised 8/29/2026 to include docstrings, cleanup comments, and fix naming conventions
"""

# First, solicit user input.
user_input = input('Provide a word for translation to Pig Latin.\n')


def to_piglatin(word: str) -> str:
    """
    Translates a given word into piglatin.

    The rules for PigLatin in this example are below, but piglatin is apparently not well defined.
    + if the word starts with a consonant, move the consonant to the end and add 'ay' afterwards i.e. pops -> opspay
    + if the word starts with a vowel, add 'yay' to the end of the word i.e. ouch -> ouchyay
    + this is apparently nonstandard, but the standard version is a bit harder.
    + TODO validate input, maybe check for special characters, multiple words?

    Args:
        word (str): The word to be translated.

    Returns:
        str: The word in piglatin.
    """

    # Provide consonants and vowels lists.
    # Notice they're all lowercase...
    # This was a good idea I stole from https://stackoverflow.com/questions/10289761/python-strings-consonants.
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"

    # the first letter is in the zero slot, convert to lowercase
    first_letter = word[0].lower()
    # if the word starts with a consonant, move it to the end and add 'ay' to the end i.e. pops -> opspay
    if first_letter in consonants:
        print(f'{word} started with a consonant')
        # if discarding capitalization of the first letter is desired, do this instead
        # word = word[1:] + firstLetter + 'ay'
        word = word[1:] + word[0] + 'ay'
        print(f'in PigLatin that\'s {word}.')
    # if the word starts with a vowel, add 'yay' to the end of the word i.e. ouch -> ouchyay  
    elif first_letter in vowels:
        print(f'{word} started with a vowel')
        word += 'yay'
        print(f'in PigLatin that\'s {word}.')
    else:
        print('Well, well, that first letter isn\'t a consonant or a vowel...')

    return word

# translate user input to piglatin
to_piglatin(user_input)

# testing...
  # toPigLatin('cat')
  # toPigLatin('oops')
  # toPigLatin('Mincemeat')