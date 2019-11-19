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
        self.add_emailtext_label()
        self.add_email_entry()
        self.add_subscribe_button()


    # Pack Method

    def add_outer_frame(self):
        # create
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure(bg="#eee", padx=10, pady=10)


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

    def add_emailtext_label(self):
        self.emailtext_label = Label(self.outer_frame)
        self.emailtext_label.grid(row=2, column=0, sticky=E)
        # ...setting the attributes of the component using the attribute
        self.emailtext_label.configure(pady=20, text="Email:")

    def add_email_entry(self):
        # create
        self.email_entry = Entry(self.outer_frame)
        self.email_entry.grid(row=2, column=1, sticky=W)
        # ...setting the attributes of the component using the attribute
        self.email_entry.configure(width=40)


# button

    def add_subscribe_button(self):
        # create
        self.subscribe_button = Button(self.outer_frame)
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+E+S+W)
        # ...setting the attributes of the component using the attribute
        self.subscribe_button.configure(bg="#ffc", text="Subscribe")



        # ...assigning any event handlers to the component
        # handle events
        # (callback functions to handle events will go here)



