from tkinter import *
from tkinter import ttk

# making the window and title of window
root = Tk()
root.title("Dec2Bin")

# making the frame window -- f = frame
f = Frame(root, bg="black")
f.pack(fill=BOTH, expand=1)

# making text next to input box -- l = label
l = Label(f, text="Decimal", bg="black", fg="white")
l.grid(row=0, column=0)

# making the entry/input box for the value
val = Entry(f, bg="white", fg="black")
val.grid(row=0, column=1)

# Dictionary to store saved numbers
saved_numbers = {}

# label for the text in submit button -- l2 = label 2
l2 = Label(f, bg="black", fg="white")
l2.grid(row=1, column=0)


def dec_to_bin(dec_num):
    """function to convert the decimal number to a binary number
    :param dec_num:

    :returns binary string:"""

    bin_str = format(int(dec_num), 'b')
    return bin_str


def deci():
    """
        Converts a decimal number entered in the text entry box to its binary equivalent
        and displays it in a Label widget. Also, updates a dictionary with the decimal
        number as key and its binary equivalent as value. Displays all saved numbers
        and their binary equivalents in a Text widget.

        Raises:
            ValueError: If the input entered in the text entry widget is not an integer.

        Returns:
            None
        """
    try:
        num = val.get()
        number = int(num)
        binary_output = dec_to_bin(number)
        l2.config(text=binary_output)

        # Update the dictionary with the new number
        saved_numbers[number] = binary_output

        # Clear the Text widget before displaying saved numbers
        saved_numbers_text.delete(1.0, END)

        # Display saved numbers in the Text widget
        for num, binary in saved_numbers.items():
            saved_numbers_text.insert(END, f"Decimal: {num}, Binary: {binary}\n")

        if number == 51:
            def hide_easteregg():
                easteregg_label.pack_forget()

            easteregg_label = Label(root, text="That's my favorite Number!", fg="white")
            easteregg_label.pack()
            root.after(2000, hide_easteregg)

    # if there is a value error, then invalid input will be displayed
    except ValueError:
        def hide_text():

            # pack_forget removes the error message from displaying in GUI
            error_label.pack_forget()

        error_label = Label(root, text="Invalid input", fg="white")
        error_label.pack()
        root.after(2000, hide_text)


# making a submit button for decimal conversion
button = Button(f, text="Submit", bg="white", fg="black", relief=FLAT, cursor="hand2", command=deci)
button.grid(row=0, column=2)

# Text widget to display saved numbers
saved_numbers_text = Text(f, height=20, width=40)
saved_numbers_text.grid(row=2, columnspan=3)

# making the window size and running the window
root.minsize(width=250, height=200)
root.maxsize(width=1000, height=500)

ttk.Button(f, text="Quit", cursor="hand2", command=root.destroy).grid(column=0, row=3)

root.mainloop()
