from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()

        # load resources
        self.plant_image = PhotoImage(file="//pclures04/home/4mahes86/Documents/Problem Solving Programming/Problem Solving/com404/0-setup/3-Interfaces/2-guis/4- images/2-swapping/plant_image.gif")
        self.plant_name_image = PhotoImage(file="//pclures04/home/4mahes86/Documents/Problem Solving Programming/Problem Solving/com404/0-setup/3-Interfaces/2-guis/4- images/2-swapping/plant_name_image.gif")

        # set window attributes
        self.title("Gui")

        # add components
        self.add_outer_frame()
        self.add_plant_image_label()
        self.add_heading_label()
        self.add_flip_button()

        # Outer Frame
    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # Label going in the outer frame Grid
    def add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=3)
        self.heading_label.configure(bg="#eee", font="Arial 15", text="Cactus Leaves")

    # Images    
    def add_plant_image_label(self):
        self.plant_image_label = Label(self.outer_frame)
        self.plant_image_label.grid(row=1, column=0)
        self.plant_image_label.configure(image=self.plant_image, height=300, width=300)

 
    # Button
    def add_flip_button(self):
        self.flip_button = Button(self.outer_frame)
        self.flip_button.grid(row=2, column=0)
        self.flip_button.configure(bg="#ffc", font="Arial 12", text="Flip")
    # Events
        self.flip_button.bind("<ButtonRelease-1>", self.__flip_button_clicked_left)
        self.flip_button.bind("<ButtonRelease-3>", self.__flip_button_clicked_right)

    # display either picture
    def __flip_button_clicked_left(self, event):
        self.plant_image_label.configure(image=self.plant_image)

    def __flip_button_clicked_right(self, event):
        self.plant_image_label.configure(image=self.plant_name_image)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()