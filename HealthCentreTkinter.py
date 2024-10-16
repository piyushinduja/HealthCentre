from tkinter import *
from tkinter.messagebox import *
import time

file_name = ""
n1 = ""


def get_date():
    import datetime
    return datetime.datetime.now()


def proceed():
    dt_ex = var.get()
    rw = var2.get()
    if (dt_ex == 0) or (rw == 0):
        showerror('Failure', "Incomplete details \n Please select at least one of the options")
    else:
        if dt_ex == 1:
            a = " Diet"
        else:
            a = " Exercise"
        if rw == 3:
            b = "r"
            read.deiconify()
            second.withdraw()
            global file_name
            file_name = n1 + a
            f = open(f"{file_name}.txt", b)
            data = f.readlines()
            y = 110
            for line in data:
                y = y + 25
                log = Label(read, text=line, font=("times new roman", 12))
                log.place(x=100, y=y)
                f.close()
        else:
            b = "a"
            write.deiconify()
            second.withdraw()


def add():
    global n1
    n1 = name.get()
    name.delete(0, END)
    dt_ex = var.get()
    rw = var2.get()
    data = text1.get()
    global file_name
    if dt_ex == 1:
        a = " Diet"
    else:
        a = " Exercise"
    if rw == 4:
        # b = "a"
        write.deiconify()
        second.withdraw()
        global file_name
        file_name = n1 + a
        f = open(f"{file_name}.txt", "a")
        f.write(str(get_date()) + ":" + data + "\n")
        f.close()
        showinfo('Success', 'Data added successfully!!')
        write.withdraw()
        first.deiconify()


def submit_name():
    global n1
    n1 = name.get()
    if (n1 == "piyush" or n1 == "modi" or n1 == "rahul" or n1 == "khushal" or n1 == "dev"):
        second.deiconify()
        first.withdraw()
    else:
        showerror('Failure', "Record doesn't exist")


# 1st page
first = Tk()
first.geometry('1000x500')
first.title("Health Centre")
wc = Label(first, text="Welcome to Health Centre", font=('times new roman', 30, 'bold',
                                                         'underline'), padx="10").pack()
log = Label(first, text="If you are an existing user then please enter your name to continue: ",
            font=('times new roman', 15), padx="5").place(x=110, y=110)
name = Entry(first, width="30")
name.place(x=500, y=150)
submit = Button(first, text="Submit", command=submit_name, font=('times new roman', 10),
                bd="5").place(x=555, y=180)
sign = Label(first, text="If not and you have to be a part of Health Centre please feel free to call +91-9082253040",
             font=('times new roman', 15), padx="5")
sign.place(x=110, y=275)

# 2nd page
second = Toplevel(first)
second.geometry('1000x500')
second.title("Health Centre")
sel1 = Label(second, text="Please select one of the following: ", font=('times new roman', 15)).place(x=110, y=110)
var = IntVar()
R1 = Radiobutton(second, font=('times new roman', 12), text="Diet", variable=var,
                 value=1)
R1.place(x=150, y=150)
R2 = Radiobutton(second, font=('times new roman', 12), text="Exercise", variable=var,
                 value=2)
R2.place(x=350, y=150)
sel2 = Label(second, text="Please select one of the following: ", font=('times new roman', 15)).place(x=110, y=310)
var2 = IntVar()
R3 = Radiobutton(second, font=('times new roman', 12), text="Read", variable=var2,
                 value=3)
R3.place(x=150, y=350)
R4 = Radiobutton(second, font=('times new roman', 12), text="Write", variable=var2, value=4)
R4.place(x=350, y=350)
second.withdraw()
btn = Button(second, text="Proceed", command=proceed, font=('times new roman', 10),
             bd="5").place(x=450, y=450)
# Read
read = Toplevel()
read.geometry('1000x500')
lbl = Label(read, text="Your diet is: ", font=('times new roman', 15)).place(x=100, y=100)
read.withdraw()
# Write
write = Toplevel()
write.geometry('1000x500')
lbl2 = Label(write, text="Please enter your data: ", font=('times new roman', 15)).place(x=100, y=100)
text1 = Entry(write, width=50)
text1.place(x=100, y=150)
btn10 = Button(write, command=add, text="Add", font=('times new roman', 10), bd="5").place(x=200, y=200)
write.withdraw()
first.mainloop()
