"""
Simple Gui Using tkinter - easy example written by Joe Manlove

created 10/29/2020
revised 11/8/2026 to add this docstring
"""

import tkinter as tk


def submit():
    """
    Provides a function to call when the submit button is pressed.
    """
    print('Submit button pressed.')
    entry = text_entry.get()
    if entry:
        display_text = f'The contents of the entry box are: {entry}.\nThe type of the contents is {type(entry)}.'
        print(display_text)
        results_label.configure(text=display_text)
    else:
        results_label.configure(text='')


# create a window
window = tk.Tk()
window.title('Testing a Title?')
window.geometry('600x600')

# creating a label widget and putting it in the window
entry_label = tk.Label(window, text="Enter some text...")
entry_label.pack()
# could also use grid or place

# create and display a text entry box
text_entry = tk.Entry(window, width=20)
text_entry.pack()

# create and display a button
submit_button = tk.Button(window, text='Submit', command=submit)
submit_button.pack()

# create and display a results label
results_label = tk.Label(window)
results_label.pack()

print('Success! Look for the window!')
# keep the window open
window.mainloop()
