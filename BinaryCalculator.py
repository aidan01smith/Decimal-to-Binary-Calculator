'''def dec_to_bin(dec_num):
    bin_str = format(int(dec_num), 'b')
    return bin_str
#basic binary converter function - maybe turn this into a class?
print(dec_to_bin(4096))'''

from tkinter import *
import tkinter as tk
from tkinter import ttk

# Creates the root window and sets the title and dimensions
root = tk.Tk()
root.title('input textbox')
root.geometry('400x200')

# Input box function
def print_input():
    inp = inputtxt.get("1.0", "end-1c")
    lbl.config(text = inp)

inputtxt = tk.Text(root,
                   height = 5,
                   width = 20)


inputtxt.pack()

# New button creation
print_button = tk.Button(root,
                         text = "Print",
                         command = print_input)


print_button.pack()


# Label creation
lbl = tk.Label(root, text = "")
lbl.pack()

root.mainloop()

'''#close button child function
ttk.Button(frame, text = "quit", command = root.destroy).grid(column = 1, row = 0)
root.mainloop()'''
