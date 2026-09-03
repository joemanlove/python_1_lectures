"""
Lecture on Try/Except

PEP 20 lines 10 and 11 say:
+ Errors should never pass silently.
+ Unless explicitly silenced.

Created on 9/3/2026 to replace an old lecture that was not good.
"""

while True:
    top = input("Enter the number you'd like on the top of the fraction:\n")
    bottom = input("Enter the number you'd like on the bottom of the fraction:\n")

    try:
      # This can cause a ValueError.
      top = int(top)
      bottom= int(bottom)

      # This can cause a ZeroDivisionError.
      result = top/bottom
    except ValueError:
      # This code executes if a ValueError occurs.
      print("Please provide an integer for both the top and bottom.")
    except ZeroDivisionError:
      # This code executes if a ZeroDivisionError occurs.
      print("The bottom of a fraction cannot be zero, please try again.")
    else:
        # This code runs if the try block succeeds.
        print(result)
        # Breaks out of the infinite loop if an acceptable result is calculated.
        break
    finally:
        # This code runs in any case.
        print("Thanks for playing.")

print("End of file, cheers!")