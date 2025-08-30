from tkinter import *

window = Tk()
window.geometry('1080x200')
window.title('main_window')

def topWindow():
    top = Toplevel()
    top.title('toplevel')
    top.geometry('1080x100')
    
    l2 = Label(top, text = 'toplevel window')

    l2.pack()
    top.mainloop()

L = Label(window, text = 'This is root window')
btn = Button(window, text = 'Click to open another window', command = topWindow)

L.pack()
btn.pack()
window.mainloop()