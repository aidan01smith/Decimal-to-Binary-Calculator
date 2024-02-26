'''def dec_to_bin(dec_num):
    bin_str = format(int(dec_num), 'b')
    return bin_str'''

'''import tkinter as tk

frame = tk.TK()
frame.title("Input Box")
frame.geometry('400x200')'''

from tkinter import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('helloworld')
root.geometry('400x200')

frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text = "hello world").grid(column = 0, row =0)
ttk.Button(frame, text = "quit", command = root.destroy).grid(column = 1, row = 0)
root.mainloop()

