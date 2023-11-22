from tkinter import *

window = Tk()
window.minsize(width=200, height=200)
window.title("Miles to kilometer converter")
window.config(pady=10, padx=10)

is_equal_to_label = Label(text="Is equal to:")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=4, row=0)

equal_entry = Label(text="0")
equal_entry.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=4, row=1)

calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=4)

window.mainloop()
