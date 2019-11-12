# GUI Interface
from tkinter import *

class Gui(Tk):
    # initialise window
    def __init__(self):
        super().__init__()

        #set windows attributes
        self.title("Newsletter")
        self.configure(bg="#eee", height=300, width=500)
        
        # add window components by
        # ...creating an object of the component stored in an attribute
        self.add_heading_label()
        self.add_newsletter_label()
        self.add_email_frame()
        self.add_emailtext_label()
        self.add_email_entry()
        self.add_subscribe_button()


    # Pack Method 

    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.pack()
        # ...setting the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 24", text="RECEIVE OUR NEWSLETTER")

    def add_newsletter_label(self):
        # create
        self.newsletter_label = Label()
        self.newsletter_label.pack()
        # ...setting the attributes of the component using the attribute
        self.newsletter_label.configure(font="Arial 11", text="Please enter your email below to receive our newsletter.")


    def add_email_frame(self):
        self.email_frame = Frame()
        self.email_frame.pack()

    def add_emailtext_label(self):
        self.emailtext_label = Label(self.email_frame)
        self.emailtext_label.pack(side=LEFT)
        # ...setting the attributes of the component using the attribute
        self.emailtext_label.configure(font="Arial 11", text="Email:")

    def add_email_entry(self):
        # create
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
        # ...setting the attributes of the component using the attribute
        self.email_entry.configure(font="Arial 11")


# button

    def add_subscribe_button(self):
        # create
        self.subscribe_button = Button(width=45)
        self.subscribe_button.pack()
        # ...setting the attributes of the component using the attribute
        self.subscribe_button.configure(bg="#ffb6c1", font="Arial 11", text="Subscribe")








        # ...assigning any event handlers to the component
        # handle events
        # (callback functions to handle events will go here)



