import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Adding an image')
root.geometry('1080x1080')
upload = Image.open("image.png")

image1 = ImageTk.PhotoImage(upload)

label = tk.Label(root, image = image1, width = 700, height = 700)
label.place(x=0, y=0)

label2 = tk.Label(root, text="This is the way to add an image to Tkinter window")
label2.place(x=0, y=0)

root.mainloop()