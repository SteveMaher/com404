# gui.py
from tkinter import *
from tkinter import messagebox

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # load resources
        self.default_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-2/Grey.gif")
        self.tick_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-2/Smile.gif")
        self.cross_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-2/Frown.gif")
        self.house_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-2/House.gif")
        self.pound_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-2/Pound.gif")
        self.euros_image = PhotoImage(file="//bbc-cs.bbc.net/bbcdata/documents/MaherS/Documents/GitHub/com404/0-setup/AE2-Review/TCA-2/Euro.gif")

        # set window properties
        self.title("Currency Converter")
        self.configure(bg="#ffe8e8")

        # add components
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_amount_label()
        self.__add_amount_entry()
        self.__add_default_image_label()
        self.__add_from_label()
        self.__add_from_optionmenu()
        self.__add_to_label()
        self.__add_to_optionmenu()
        self.__add_buttons_frame()
        self.__add_clear_button()
        self.__add_message_box_label()
        self.__add_convert_button()
        self.__add_animation_button()
        self.__add_animation_frame()

    # Outer frame 
    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0) 
        self.outer_frame.configure(bg="#ffe8e8", height=400, width=500, padx=10, pady=10)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=1, columnspan=2) 
        self.heading_label.configure(bg="#ffe8e8", font="Arial 18", text="Currency Converter:", padx=54)

    def __add_amount_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0, columnspan=2, sticky=W)
        self.instruction_label.configure(bg="#ffe8e8", font="Arial 10", text="Amount")

    #Entry Function
    def __add_amount_entry(self):
        self.amount_entry = Entry(self.outer_frame)
        self.amount_entry.grid(row=2, column=0, columnspan=5, sticky=W)
        self.amount_entry.configure(fg="#f00", width=50)
        self.amount_entry.bind("<KeyRelease>", self.__amount_keyboard_entry)
      
    # Add image label to Frame with grid
    def __add_default_image_label(self):
        self.default_image_label = Label(self.outer_frame)
        self.default_image_label.grid(row=2, column=4)
        self.default_image_label.configure(image=self.default_image, height=15, width=15) 

    def __amount_keyboard_entry(self, event):
        response = self.amount_entry.get()
        if response == "":
            self.default_image_label.configure(image=self.cross_image)
        else:
            self.default_image_label.configure(image=self.tick_image)
 
    def __add_from_label(self):
        self.from_label = Label(self.outer_frame)
        self.from_label.grid(row=3, column=0, columnspan=2, sticky=W)
        self.from_label.configure(bg="#ffe8e8", font="Arial 10", text="From")       

    def __add_from_optionmenu(self):
        self.SelectionVar = StringVar()
        self.SelectionVar.set("GBP")
        self.from_optionmenu = Spinbox(self.outer_frame, textvariable=self.SelectionVar, values=("GBP", "Euros"))
        self.from_optionmenu.grid(row=4, column=0, columnspan=5, sticky=W)
        self.from_optionmenu.configure(width=50)

    def __add_to_label(self):
        self.to_label = Label(self.outer_frame)
        self.to_label.grid(row=5, column=0, columnspan=2, sticky=W)
        self.to_label.configure(bg="#ffe8e8", font="Arial 10", text="To")       

    def __add_to_optionmenu(self):
        self.Selection2Var = StringVar()
        self.Selection2Var.set("Euros")
        self.to_optionmenu = Spinbox(self.outer_frame, textvariable=self.Selection2Var, values=("Euros", "USD"))
        self.to_optionmenu.grid(row=6, column=0, columnspan=5, sticky=W)
        self.to_optionmenu.configure(width=50)

    # Button1 Frame
    def __add_buttons_frame(self):
        self.buttons_frame = Frame(self.outer_frame)
        self.buttons_frame.grid(row=7, column=0, columnspan=4, sticky=N+E+S+W)
        self.buttons_frame.configure(bg="#ffe8e8", padx=80, pady=20)

    def __add_clear_button(self):
        self.clear_button = Button(self.buttons_frame)
        self.clear_button.pack(side=LEFT)
        self.clear_button.configure(bg="#FFF", text="Clear", width=10)
        self.clear_button.bind("<Button-1>", self.__clear_button_clicked)

    def __add_convert_button(self):
        self.convert_button = Button(self.buttons_frame)
        self.convert_button.pack(side=RIGHT)
        self.convert_button.configure(bg="#FFF", text="Convert", width=10) 
        self.convert_button.bind("<Button-1>", self.__convert_button_clicked)

    def __add_message_box_label(self):
        self.MessageVar = StringVar()
        self.MessageVar.set("\nSystem Message Displayed Here\n")
        self.message_box_label = Message(self.outer_frame)
        self.message_box_label.grid(row=8, column=0, columnspan=5, sticky=N+E+S+W, pady=10)
        self.message_box_label.configure(bg="#fffbce", fg="blue", relief=SUNKEN, textvariable=self.MessageVar, width=200)

    def __convert_button_clicked(self, event):
        currencyfrom = self.from_optionmenu.get()
        currencyto = self.to_optionmenu.get()
        amount = int(self.amount_entry.get())
        if currencyfrom == "GBP" and currencyto == "Euros":
            rate = 1.15
            result = amount *1.15
        elif currencyfrom == "GBP" and currencyto == "USD":
            rate = 1.42
            result = amount *1.42
        elif currencyfrom == "Euros" and currencyto == "USD":
            rate = 1.24
            result = amount *1.24
        elif currencyfrom == "Euros" and currencyto == "Euros":
            result = "error"
        converting = self.__convert_button_clicked
        if converting != "" and result != "error":
            self.MessageVar.set("\nConverting...\n")
            messagebox.showinfo("Output", "" + str(amount) + " from " + str(currencyfrom) + " to " + str(currencyto) + " with rate of " + str(rate) + " is " + format(result, '.2f') + ".")
        elif converting != "" and result == "error":
            messagebox.showerror("Error", "Please try again") 
        else:
            self.MessageVar.set("\nSystem Message Displayed Here\n")
            
    def __clear_button_clicked(self, event):
        clearing = self.__clear_button_clicked
        if clearing != "":
            self.MessageVar.set("\nSystem Message Displayed Here\n")
            self.amount_entry.delete(0, 'end')
    
    def __add_animation_button(self):
        self.animation_button = Button(self.outer_frame)
        self.animation_button.grid(row=9, column=1, columnspan=2, padx=10)
        self.animation_button.configure(bg="white", text="Simulate", width=14, padx=10) 
        self.animation_button.bind("<Button-1>", self.__animation_button_clicked)

    # Animation Frame
    def __add_animation_frame(self):
        self.animation_frame = Frame(self.outer_frame)
        self.animation_frame.grid(row=10, column=0, columnspan=5) 
        self.animation_frame.configure(bg="#BDFCC9", height=200, width=360, padx=10, pady=10)
   
    def __animation_button_clicked(self, event):
        currencyfrom = self.from_optionmenu.get()
        animation = self.__animation_button_clicked
        self.house_image_label = Label(self.animation_frame)
        self.house_image_label.place(x = 270, y = 50)
        self.house_image_label.configure(image=self.house_image) 
        if animation != "" and currencyfrom == "GBP":
            self.pound_image_label = Label(self.animation_frame)
            self.pound_image_label.place(x=self.image_x_pos, y=self.image_y_pos)
            self.pound_image_label.configure(image=self.pound_image) 
            self.tick1()
        if animation != "" and currencyfrom == "Euros":
            self.euros_image_label = Label(self.animation_frame)
            self.euros_image_label.place(x=self.image_x_pos, y=self.image_y_pos)
            self.euros_image_label.configure(image=self.euros_image) 
            self.tick2()

    # the timer tick function    
    def tick1(self):
        if self.image_x_pos > 4 and self.image_x_pos < 252:
            self.image_x_change = 1
            self.image_x_pos = self.image_x_pos + self.image_x_change
            self.pound_image_label.place(x=self.image_x_pos, y=self.image_y_pos)
            self.after(100, self.tick1)
    
    def tick2(self):
        if self.image_x_pos > 4 and self.image_x_pos < 252:
            self.image_x_change = 1
            self.image_x_pos = self.image_x_pos + self.image_x_change
            self.euros_image_label.place(x=self.image_x_pos, y=self.image_y_pos)
            self.after(100, self.tick2)       


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()      