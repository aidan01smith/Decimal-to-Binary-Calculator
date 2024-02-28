'''def dec_to_bin(dec_num):
    bin_str = format(int(dec_num), 'b')
    return bin_str
#basic binary converter function - maybe turn this into a class?
print(dec_to_bin(4096))'''


from tkinter import *
from tkinter import ttk

#making the window and title of window
root = Tk()
root.title("Dec2Bin")

#making the window black fill
f = Frame(root, bg = "black")
f.pack(fill = BOTH, expand=1)

#making text next to input box
l = Label(f, text = "Decimal", bg = "black", fg = "white")
l.grid(row = 0, column = 0)

#making the entry/input box for the value
val = Entry(f)
val.grid(row = 0, column = 1)

def deci():
    num = val.get()
    number = int(num)
    a = []
    while number > 0:
        p = number % 2
        a.append(p)
        number = number // 2  # Integer division
    a.reverse()
    l2.config(text=a)


#making a submit button for decimal conversion
button = Button(f, text = "Submit", bg = "black", fg = "white", relief = FLAT, cursor = "hand2", command = deci)
button.grid(row = 0, column = 2)

l2 = Label(f, bg = "black", fg = "white")
l2.grid(row = 1, column = 0)

#making the window size and running the window
root.minsize(width = 250, height = 100)
root.maxsize(width = 1000, height = 100)

ttk.Button(f, text = "quit", command = root.destroy).grid(column = 0, row = 2)

root.mainloop()
