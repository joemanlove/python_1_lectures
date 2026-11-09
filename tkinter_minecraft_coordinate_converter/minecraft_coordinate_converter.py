"""
Minecraft Coordinate Converter - a medium difficulty tkinter example written by Joe Manlove

created 10/29/2020
tested on repl 10/30/2020, image placement doesn't quite work on repl (rip repl.it, we loved you before the AI slopocalypse)
Revised 11/8/2026 to add this docstring and modernize filepath fixes
"""

import tkinter as tk

from pathlib import Path
# Make a Path object out of the script's location.
SCRIPT_PATH = Path(__file__)
# Make a Path object for the Folder the script is in.
DIRECTORY_PATH = SCRIPT_PATH.resolve().parent
# MAke a Path object to the background image
BACKGROUND_IMAGE_PATH = DIRECTORY_PATH / "background800_649.gif"

class ThreeButtonMenu:
    """
    Provides a label, three entry boxes, and a button to convert coordinates.
        parameters: window - a Tk object; relative_x - a float in 0,1; relative_y - a float in 0,1; name - a string

    In order to function properly, the set_target method should be called on another ThreeButtonMenu.
    window should be the Tk object for the Gui.
    realtive_x and relative_y position the menu in the window.
    name is a string for formatting buttons.
    coordinates are rounded down.
    Note, minecraft y (the vertical coordinate) is not effected by nether conversion.
    """

    def __init__(self, window, relative_x, relative_y, name):
        # size of entry boxes
        ENTRY_LENGTH = 10

        # where are we converting to, changed using the set_target method
        self.target = self
        self.factor = 1

        # Used to label the menu
        self.name = name

        # String Variables for entry box text
        self.x_text = tk.StringVar()
        self.y_text = tk.StringVar()
        self.z_text = tk.StringVar()

        # Frame
        self.containing_frame = tk.Frame(window)
        self.containing_frame.place(
            relx=relative_x, rely=relative_y, anchor='n')

        # label
        self.label = tk.Label(self.containing_frame,
                              text=f"{self.name} Coordinates")
        self.label.grid(row=0, column=0, columnspan=3, padx=2, pady=2)

        # entry boxes
        self.x_entry = tk.Entry(self.containing_frame,
                                width=ENTRY_LENGTH, textvariable=self.x_text)
        self.x_entry.grid(row=1, column=0, padx=2, pady=2)
        self.y_entry = tk.Entry(self.containing_frame,
                                width=ENTRY_LENGTH, textvariable=self.y_text)
        self.y_entry.grid(row=1, column=1, padx=2, pady=2)
        self.z_entry = tk.Entry(self.containing_frame,
                                width=ENTRY_LENGTH, textvariable=self.z_text)
        self.z_entry.grid(row=1, column=2, padx=2, pady=2)

        # button
        self.button = tk.Button(self.containing_frame, background='green',
                                text='Convert Coordinates', command=self.convert)
        self.button.grid(row=2, column=0, columnspan=3, padx=2, pady=2)

        self.error_label = tk.Label(
            self.containing_frame, fg='red', font=("Times", 15))

    def set_target(self, target, factor):
        """
        Sets the target for placing the converted coordinates into and also sets the conversion factor.
        
        Args:
            target (ThreeButtonMenu): The Three Button Menu where output will appear.
            factor (Float): The conversion factor between the two coordinate systems.
        """

        self.target = target
        self.factor = factor
        self.button.config(text=f'Convert to {target.name} Coordinates')

    def convert(self):
        """
        Converts the text in the entry boxes by the factor, updates target entry boxes.
        """

        # get the text that's in the entry boxes.
        x = self.x_text.get()
        y = self.y_text.get()
        z = self.z_text.get()

        # try to typecast and convert each coordinate that was present.
        try:
            if x:
                x = int(x)
                self.target.x_text.set(round(self.factor * x))
            if y:
                # minecraft y is not effected by this
                y = int(y)
                self.target.y_text.set(y)
            if z:
                z = int(z)
                self.target.z_text.set(round(self.factor * z))

        # if typecast fails, update and display the error label.
        except ValueError:
            self.error_label.configure(text="Error, non-numeric value.")
            self.error_label.grid(row=3, column=0, columnspan=3)

        # if the try block executes without error, remove the error_label from view.
        else:
            self.error_label.grid_forget()
            self.target.error_label.grid_forget()


# make the main window to hold everything
window = tk.Tk()
window.title('Overworld <-> Nether Coordinate Converter')

# default window size.
window.geometry('600x550')

# Max/Min window size
window.maxsize(800, 649)
window.minsize(450, 150)


# make the background image. This is surprisingly frustrating.
background_photo = tk.PhotoImage(file=BACKGROUND_IMAGE_PATH)
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)
# making this resizable would be good:
# see https://stackoverflow.com/questions/53783227/tkinter-overlaying-a-label-on-top-of-a-background-image

# make menus
overworld = ThreeButtonMenu(window, .25, .3, "Overworld")
nether = ThreeButtonMenu(window, .75, .3, "Nether")

# point them at each other
overworld.set_target(nether, 1 / 8)
nether.set_target(overworld, 8)

print('Success, go find the window...')

window.mainloop()
