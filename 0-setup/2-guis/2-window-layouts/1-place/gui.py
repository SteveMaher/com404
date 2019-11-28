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

        self.add_background()
        self.add_heading_label()
        self.add_newsletter_label()
        self.add_emailtext_label()
        self.add_email_entry()
        self.add_subscribe_button()



    def add_background(self):
        self.background = Canvas(width=400)
        self.background.place(x=0, y=0)
        self.background.configure(bg="#e0eeee")

    def add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.place(x=20, y=22)
        # ...setting the attributes of the component using the attribute
        self.heading_label.configure(font="Arial 24", text="RECEIVE OUR NEWSLETTER")

    def add_newsletter_label(self):
        # create
        self.newsletter_label = Label()
        self.newsletter_label.place(x=70, y=110)
        # ...setting the attributes of the component using the attribute
        self.newsletter_label.configure(font="Arial 11", text="Please enter your email below to receive our newsletter.")

    def add_emailtext_label(self):
        # create
        self.emailtext_label = Label()
        self.emailtext_label.place(x=70, y=200)
        # ...setting the attributes of the component using the attribute
        self.emailtext_label.configure(font="Arial 11", text="Email:")

    def add_email_entry(self):
        # create
        self.email_entry = Entry(width=30)
        self.email_entry.place(x=130, y=200)
        # ...setting the attributes of the component using the attribute
        self.email_entry.configure(font="Arial 11")

    def add_subscribe_button(self):
        # create
        self.subscribe = Button(width=45)
        self.subscribe.place(x=20, y=270)
        # ...setting the attributes of the component using the attribute
        self.subscribe.configure(bg="#ffb6c1", font="Arial 11", text="Subscribe")





        # ...assigning any event handlers to the component
        # handle events
        # (callback functions to handle events will go here)



