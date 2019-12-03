from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.ambulance_image = PhotoImage(file="U:/Documents/Problem Solving Programming/com404/0-setup/2-guis/4-images/1-loading/ambulance.gif")
        self.bike_image = PhotoImage(file="U:/Documents/Problem Solving Programming/com404/0-setup/2-guis/4-images/1-loading/bike.gif")
        self.plane_image = PhotoImage(file="U:/Documents/Problem Solving Programming/com404/0-setup/2-guis/4-images/1-loading/plane.gif")

        # set window attributes
        self.title("Gui")

        # add components
        self.add_outer_frame()
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()
        self.add_heading_label()

        # Outer Frame
    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # Label going in the outer frame Grid
    def add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(bg="#eee", font="Arial 15", text="TRANSPORT")

    # Images    
    def add_ambulance_image_label(self):
        self.ambulance_image_label = Label(self.outer_frame)
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(image=self.ambulance_image, height=60, width=60)

    def add_bike_image_label(self):
        self.bike_image_label = Label(self.outer_frame)
        self.bike_image_label.grid(row=1, column=1)
        self.bike_image_label.configure(image=self.bike_image, height=60, width=60)
 
    def add_plane_image_label(self):
        self.plane_image_label = Label(self.outer_frame)
        self.plane_image_label.grid(row=1, column=2)
        self.plane_image_label.configure(image=self.plane_image, height=60, width=60)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()