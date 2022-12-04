from tkinter import *


def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(height=300, width=500)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.config(text="New Text")                            # this changes text
# my_label.pack()
my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Button 2
button_2 = Button(text="New Button")
button_2.grid(column=2, row=0)

# Entry
entry = Entry(width=10)
# entry.pack()
entry.grid(column=3, row=2)


window.mainloop()
