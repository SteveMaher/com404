# gui.py
from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.default_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-1/Grey.gif")

        # set window properties
        self.title("Newsletter")
        self.configure(bg="#ccc", height= 220, width=360, padx=10, pady=10)

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_email_frame()
        self.__add_email_label()
        self.__add_email_entry()
        self.__add_default_image_label()
        self.__add_subscribe_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)
        self.outer_frame.configure( bg="#eee", padx=10, pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(font="Arial 14", text="RECEIVE OUR NEWSLETTER", padx=10, pady=10)

    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#eee", text="Please enter your email below to receiver our newsletter", padx=10, pady=10)

    # Create Frame
    def __add_email_frame(self):
        self.email_frame = Frame(self.outer_frame)
        self.email_frame.grid(row=2, column=0)

    # Add lable to Frame with pack
    def __add_email_label(self):
        self.email_label = Label(self.email_frame)
        self.email_label.pack(side = LEFT)
        self.email_label.configure(text="Email:", padx=10, pady=10)

    # Add lable to Frame with pack
    def __add_email_entry(self):
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side = RIGHT)
        self.email_entry.configure(fg="#f00", width = 30)

    # Add image lable to Frame with pack
    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2, column=1, sticky=W)
        #self.default_image_label.pack(side = RIGHT)
        self.default_image_label.configure(image=self.default_image, height=15, width=15, padx=10, pady=10)

    # Add button to window outside the outer frame
    def __add_subscribe_button(self):
        self.subscribe_button = Button()
        self.subscribe_button.grid(row=3, column=0, columnspan=2, sticky=N+S+E+W)
        self.subscribe_button.configure(bg="#fcc", text="Subscribe")
        self.subscribe_button.bind("<ButtonRelease-1>", self.__subscribe_button_clicked)

    def __subscribe_button_clicked(self, event):
        messagebox.showinfo("Tickets", "Subscribed!")


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()



