"""
Adding an Image to a tkinter window written by Joe Manlove

created 10/30/2020
revised 11/08/2026 to add this docstring and fix filepath issues using the modern filepath solution
"""
import tkinter as tk
from pathlib import Path


# Make a Path object out of the script's location.
SCRIPT_PATH = Path(__file__)
# Make a Path object for the Folder the script is in.
DIRECTORY_PATH = SCRIPT_PATH.resolve().parent
# Make a Path object pointing to the image
IMAGE_PATH = DIRECTORY_PATH / "sd_pi2.png"


window = tk.Tk()
window.geometry("300x300")

sd_image = tk.PhotoImage(file=IMAGE_PATH)
image_label = tk.Label(window, image=sd_image)
image_label.place(relx=.5, rely=.5, anchor='center')

test_label = tk.Label(text="Testing...")
test_label.grid(row=0, column=0)

window.mainloop()
