# GUI Interface
from tkinter import *

class Gui(Tk):
    # initialise window
    def __init__(self):
        super().__init__()

        #set windows attributes
        self.title("Newsletter")
        self.configure(bg="#ccc", padx=10, pady=10)
        
        # add window components by
        # ...creating an object of the component stored in an attribute
        self.add_outer_frame()
        self.add_heading_label()
        self.add_newsletter_label()
        self.add_email_frame()
        self.add_emailtext_label()
        self.add_email_entry()
        self.add_subscribe_button()

    # Grid - this is the outer frame
    def add_outer_frame(self):
        # create
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)

    # Pack - this is the inner frame
    def add_email_frame(self):
        self.email_frame = Frame(self.outer_frame)
        self.email_frame.grid(row=2, column=0)

    # Grid - these are going in the outer frame
    def add_heading_label(self):
        # create
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        # ...setting the attributes of the component using the attribute
        self.heading_label.configure(bg="#eee", font="Arial 18", text="RECEIVE OUR NEWSLETTER")

    def add_newsletter_label(self):
        # create
        self.newsletter_label = Label(self.outer_frame)
        self.newsletter_label.grid(row=1, column=0, columnspan=2, sticky=W)
        # ...setting the attributes of the component using the attribute
        self.newsletter_label.configure(bg="#eee", text="Please enter your email below to receive our newsletter.")   


    # Pack - These two are going in the inner frame 
    def add_emailtext_label(self):
        self.emailtext_label = Label(self.email_frame)
        self.emailtext_label.pack(side=LEFT)
        # ...setting the attributes of the component using the attribute
        self.emailtext_label.configure(font="Arial 10", text="Email:")

    def add_email_entry(self):
        # create
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
        # ...setting the attributes of the component using the attribute
        self.email_entry.configure(width=40)


    # button - This is going in the inner frame
    def add_subscribe_button(self):
        # create
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        # ...setting the attributes of the component using the attribute
        self.subscribe_button.configure(bg="#ffc", text="Subscribe")



        # ...assigning any event handlers to the component
        # handle events
        # (callback functions to handle events will go here)



