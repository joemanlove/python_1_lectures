"""
Fibonacci and Recursion Lecture written by Joe Manlove
created 7/17/2020
revised 7/17/2020 after video to fix issues
  issue 1: misspelling of fibonacci was confusing
  issue 2: testing lines were being run on import
      added if __name__ == "__main__" to fix
revised 7/18/2020 to fix comment on the time taken to compute
revised 10/14/2026 
"""

# The fibonacci sequence:
# number: 0  1  2  3  4  5  6  7
# element: 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(n):
    """
    The first two cases are 0 -> 0, 1-> 1, otherwise an element is the sum of the previous two.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# stops this code from running on import
if __name__ == '__main__':
    # calculate the first 100 as a test (this will take an extremely long time)
    for i in range(100):
        print(f'The {i}th Fibonacci number is {fibonacci(i)}.')
