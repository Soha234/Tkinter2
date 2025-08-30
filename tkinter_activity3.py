from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('10800x200')
root.title('Alertbox')
def msg():
    messagebox.showwarning('Alert', 'A virus has been detected.', icon = "info")

button = Button(root, text='Scan for virus', command = msg)
button.pack()

root.mainloop()