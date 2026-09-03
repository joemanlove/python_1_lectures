"""
Lecture on Basic Functions in Python

Created 9/3/2026
"""

def sum_of_digits(n: int) -> int:
    """
    Returns the sum of the digits of a provided integer.

    Args:
        n (int): The integer to sum digits of.

    Returns:
        int: The sum of the digits.
    """
    # String cast in order to be able to iterate.
    n_as_string = str(n)
    
    total = 0

    # Go through the number one digit at a time adding to total.
    for char in n_as_string:
        total += int(char)

    return total

def reverse_string(s: str) -> str:
    """
    Returns a reversed version of a string.

    Args:
        s (str): The string to be reversed.
    Returns:
        str: The reversed string.
    """
    # Use string slicing to go through the whole string backwards.
    return s[::-1]



if __name__ == "__main__":
    print(reverse_string("This is test."))

    print(sum_of_digits(6548231234))