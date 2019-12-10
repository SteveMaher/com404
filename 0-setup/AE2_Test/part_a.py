# gui.py
from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.santa_image = PhotoImage(file="//pclures04/home/4mahes86/Documents/Problem Solving Programming/com404/0-setup/AE2_Test/santa.gif")
   
        # set window properties
        self.title("Letter to Santa")
        self.configure(bg="#f66", height= 500, width=400, padx=15, pady=15)

        # add components
        self.__add_global_frame()
        self.__add_heading_label()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_santa_image_label()
        self.__add_letter_text()
        self.__add_post_button()
     
    def __add_global_frame(self):
        self.global_frame = Frame()
        self.global_frame.grid(row=0, column=0)
        self.global_frame.configure( bg="#f33", padx=5, pady=5)

    # Add lable to grid
    def __add_heading_label(self):
        self.heading_label = Label(self.global_frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        self.heading_label.configure(bg="#f33", fg="#fff", font="Arial 18", text="Write to Santa!", pady=5)

    # Add lable to grid
    def __add_name_label(self):
        self.name_label = Label(self.global_frame)
        self.name_label.grid(row=1, column=0, sticky=W)
        self.name_label.configure(bg="#f33", fg="#fff", font="Arial 12", text="Your name:", pady=5)

    # Add entry box to grid
    def __add_name_entry(self):
        self.name_entry = Entry(self.global_frame)
        self.name_entry.grid(row=1, column=1, sticky=N+S+E+W)
        self.name_entry.configure()
       
    # Add image lable to grid
    def __add_santa_image_label(self):
        self.santa_image_label = Label(self.global_frame)
        self.santa_image_label.grid(row=2, column=0, sticky=W)
        self.santa_image_label.configure(image=self.santa_image, bg="#f33")

    # Add lettet text box to grid
    def __add_letter_text(self):
        self.letter_text = Text(self.global_frame)
        self.letter_text.grid(row=2, column=1, sticky=E)
        self.letter_text.configure(height=5, width=30)

    # Add button to window outside the global frame
    def __add_post_button(self):
        self.post_button = Button()
        self.post_button.grid(row=3, column=0, columnspan=2, sticky=N+S+E+W)
        self.post_button.configure(bg="#ff0", text="Post Letter")
        self.post_button.bind("<ButtonRelease-1>", self.__post_button_clicked)

    # Define message
    def __post_button_clicked(self, event):
        messagebox.showinfo("Sent!", "Your letter has been sent!")























if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()