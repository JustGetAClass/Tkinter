from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(height=300, width=500)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24))
my_label.config(text="New Text")                            # this changes text
my_label["text"] = "New text"                               # or this
my_label.pack()


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()


window.mainloop()
