# GUI Interface
from tkinter import *
from tkinter import messagebox


class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        #set windows attributes
        self.title("Tickets")
        self.configure(bg="#ccc", padx=10, pady=10)
        
        # add components
        self.add_outer_frame()
        self.add_heading_label()
        self.add_instruction_label()
        self.add_ticket_entry()
        self.add_buy_button()
     
    # Outer Frame
    def add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # These are going in the outer frame, Grid

    def add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#eee", font="Arial 18", text="Entrance Ticket")

    def add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#eee", text="How many tickets are needed?")   


    def add_ticket_entry(self):
        self.ticket_entry = Entry(self.outer_frame)
        self.ticket_entry.grid(row=2, column=0, sticky=W)
        self.ticket_entry.configure(width=40)


    def add_buy_button(self):
        # Create
        self.buy_button = Button(self.outer_frame)
        self.buy_button.grid(row=3, column=0, columnspan=2)
        # Style
        self.buy_button.configure(bg="#ffc", text="Submit")

        # Events
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        response = int(self.ticket_entry.get())
        if response == 1:
            messagebox.showinfo("Purchased", "You have purchased 1 ticket!")
        elif response >= 2:
            messagebox.showinfo("Purchased", "You have purchased " + str(response) + " tickets!")
        else:
            messagebox.showinfo("Purchased", "You have entered an invalid number of tickets!")



