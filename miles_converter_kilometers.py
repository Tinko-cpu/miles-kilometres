from tkinter import *


def mile_kilo():
    miles = miles_entry.get()
    km = int(miles) * 1.609
    equal_entry.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.title("Miles to kilometer converter")
window.config(pady=10, padx=10)

is_equal_to_label = Label(text="Is equal to:", font=("Arial", 12, "bold"))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=4, row=0)

equal_entry = Label(text="0")
equal_entry.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=4, row=1)

calculate_button = Button(text="Calculate", command=mile_kilo, font=("Arial", 12, "bold"))
calculate_button.grid(column=1, row=4)

window.mainloop()
