from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.bus_image = PhotoImage(file="//pclures04/home/4mahes86/Documents/Problem Solving Programming/Problem Solving/com404/0-setup/3-Interfaces/2-guis/4- images/3-positioning/bus_image.gif")
        self.map_image = PhotoImage(file="//pclures04/home/4mahes86/Documents/Problem Solving Programming/Problem Solving/com404/0-setup/3-Interfaces/2-guis/4- images/3-positioning/map_image.gif")

        # set window attributes
        self.title("Gui")

        # add components
        self.add_outer_frame()
        self.add_bus_image_label()
        self.add_map_label()
        
        #self.add_flip_button()

        # Outer Frame
    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # Label going in the outer frame Grid
    def add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(bg="#eee", font="Arial 15", text="Bus Journey")

   















# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()