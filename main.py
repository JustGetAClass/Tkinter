import tkinter


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(height=300, width=500)
# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.pack()


window.mainloop()
