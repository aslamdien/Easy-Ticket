# Easy Ticket
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ticket Sales")
root.geometry("500x600")

class Ticket:

    result = StringVar()
    tic = StringVar()
    cellno = StringVar()

    def __init__(self, master):
        # Cell number
        # - Label For the Cell Number -
        self.lab1 = Label(master, text = "Enter Your Cell Number")
        self.lab1.place(x=5, y=20)

        # Entry For Cell Number
        self.cell_number = Entry(master)
        self.cell_number.place(x=200, y=20)

        # Event Ticket
        # - Label For Category -
        self.lab2 = Label(master, text = "Select Ticket Category")
        self.lab2.place(x=5, y=70)

        # Selection Box For Event
        self.category = ["Soccer", "Movies", "Theater"] # Options to choice from
        self.values = StringVar(root)
        self.values.set("Select Ticket") # Default Setting
        self.opt = OptionMenu(root, self.values, *self.category) # Type of Selection Box
        self.opt.place(x=200, y=70)

        # Number Of Ticket
        # - Label For Tickets -
        self.lab3 = Label(master, text = "Number of Tickets")
        self.lab3.place(x=5, y=120)

        # - Entry/Spinbox For Ticket
        self.nr_tickets = Spinbox(master, from_= 0, to = 99)
        self.nr_tickets.place(x=200, y=120)

        # Output
        # Label for Amount Payable
        self.lab4 = Label(master, text = "Amount Payable:")
        self.lab4.place(x=5, y=400)
        # Label For text-variable of Price to Pay
        self.lab5 = Label(master, text = "", width = "13", textvariable = self.result)
        self.lab5.place(x=150, y=400)

        # Label For "Reservation for"
        self.lab6 = Label(master, text = "Reservation for")
        self.lab6.place(x=5, y=450)
        # Label for text-variable of number of tickets
        self.lab7 = Label(master, text = "tickets", width = "10", textvariable = self.tic)
        self.lab7.place(x=150, y=450)
        # Label for "Was Done By"
        self.lab8 = Label(master, text = "Was Done By")
        self.lab8.place(x=5, y=500)
        # Label for text-variable  of Cell number
        self.lab9 = Label(master, text = "", width = "15", textvariable = self.cellno)
        self.lab9.place(x=150, y=500)

        # Borders for Entry Answers
        self.lab10 = Label(master, text = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.lab10.place(x=3, y=370)
        self.lab11 = Label(master, text = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.lab11.place(x=3, y=530)

        # Buttons
        self.btn1 = Button(master, text = "Calculate Ticket", command = self.price)
        self.btn1.place(x=15, y=200)
        self.btn2 = Button(master, text = "Clear Entries", command = self.clear)
        self.btn2.place(x=200, y=200)


    # Definitions Of Commands For Buttons
    # For Tickets
    def tick(self):
        tic = self.nr_tickets.get()
        self.tic.set(tic)

    # For Cell Number
    def phone(self):
        num = self.cell_number.get()
        self.cellno.set(num)

    # For Cost OF Tickets
    def price(self):
        self.tick()
        self.phone()

        if self.values.get() == "Soccer":
            result = float(self.nr_tickets.get()) * 40 + 0.14 * (float(self.nr_tickets.get()) * 40)
            self.result.set(result)

        elif self.values.get() == "Movies":
            result = float(self.nr_tickets.get()) * 75 + 0.14 * (float(self.nr_tickets.get()) * 75)
            self.result.set(result)

        elif self.values.get() == "Theater":
            result = float(self.nr_tickets.get()) * 100 + 0.14 * (float(self.nr_tickets.get()) * 100)
            self.result.set(result)

    def clear(self):
        self.cell_number.delete(0, END)
        self.nr_tickets.delete(0, END)
        self.nr_tickets.insert(0, 0)
        self.values.set("Select Ticket")
        self.result.set("")
        self.tic.set("")
        self.cellno.set("")


x = Ticket(root)
root.mainloop()
