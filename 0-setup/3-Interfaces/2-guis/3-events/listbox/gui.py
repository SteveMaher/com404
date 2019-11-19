# GUI Interface
from tkinter import *
from tkinter import messagebox


class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        #set windows attributes
        self.title("Song Maker")
        self.configure(bg="#ccc", padx=10, pady=10)
        
        # add components
        self.add_outer_frame()
        self.add_heading_label()
        self.add_lyric_to_add_label()
        self.add_lyric_to_add_entry()
        self.add_add_button()
        self.add_lyric_label()
        self.add_lyric_box()
     
    # Outer Frame with 2 columns
    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=1)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # These are going in the outer frame, Grid
    def add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 18", text="Song Maker")

    def add_lyric_to_add_label(self):
        self.lyric_to_add_label = Label(self.outer_frame)
        self.lyric_to_add_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.lyric_to_add_label.configure(bg="#eee", text="Lyric to add:")

    def add_lyric_to_add_entry(self):
        self.ticket_entry = Entry(self.outer_frame)
        self.ticket_entry.grid(row=2, column=0, sticky=W)
        self.ticket_entry.configure(width=40)

    def add_button(self):
        self.add_button = Button(self.outer_frame)
        self.add_button.grid(row=2, column=2, columnspan=2)
        self.addy_button.configure(bg="#ffc", text="Add")


    def add_lyric_label(self):
        self.lyric_label = Label(self.outer_frame)
        self.lyric_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.lyric_label.configure(bg="#eee", text="Lyrics:")


# List Box ???
    def add_lyric_box(self):
        self.lyric_box = Entry(self.outer_frame)
        self.lyric_box.grid(row=4, column=0, sticky=W)
        self.lyric_box.configure(width=40)



        # Events
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_button_clicked(self, event):
        response = int(self.ticket_entry.get())
        if response == 1:
            messagebox.showinfo("Purchased", "You have purchased 1 ticket!")
        elif response >= 2:
            messagebox.showinfo("Purchased", "You have purchased " + str(response) + " tickets!")
        else:
            messagebox.showinfo("Purchased", "You have entered an invalid number of tickets!")

