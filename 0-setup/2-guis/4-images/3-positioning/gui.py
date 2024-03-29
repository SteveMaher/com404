# GUI interface
from tkinter import *
from tkinter import messagebox

class Gui(Tk):

# initialise window
    def __init__(self):
        super().__init__()

# load resources
        #self.bus_image = PhotoImage(file="\\bbc-cs.bbc.net\bbcdata\documents\MaherS\Documents\GitHub\com404\0-setup\2-guis\4-images\3-positioning\bus_image.gif")
        #self.map_image = PhotoImage(file="\\bbc-cs.bbc.net\bbcdata\documents\MaherS\Documents\GitHub\com404\0-setup\2-guis\4-images\3-positioning\map_image.gif")
        self.bus_image = PhotoImage(file="U:/Documents/Problem Solving Programming/com404/0-setup/2-guis/4-images/3-positioning/bus_image.gif")
        self.map_image = PhotoImage(file="U:/Documents/Problem Solving Programming/com404/0-setup/2-guis/4-images/3-positioning/map_image.gif")

# set window attributes
        self.title("Gui")
        self.configure(bg="#ccc")

# add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_map_frame()
        self.__add_map_image_label()
        self.__add_bus_image_label()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
  
# Heading function
    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0)
        self.heading_label.configure(font="Arial 16", text="Bus Journey")

# Frame function
    def __add_map_frame(self):
        self.map_frame = Frame(self.outer_frame)
        self.map_frame.grid(row=1, column=0)
        self.map_frame.configure(bg="#eee", width=800, height=600)

    def __add_map_image_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(image=self.map_image)

    def __add_bus_image_label(self):
        self.bus_image_label = Label(self.map_frame)
        self.bus_image_label.place(x=20, y=20)
        self.bus_image_label.configure(image=self.bus_image)
        self.bus_image_label.bind("<B1-Motion>", self.__bus_move)

    def __bus_move(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is " + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is " + str(event.y))
        self.bus_image_label.place(x=event.x, y=event.y)

# Create an object of the Gui class when this module is executed
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()