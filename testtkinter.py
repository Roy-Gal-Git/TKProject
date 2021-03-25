import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
frame = tk.Frame(root)
file1 = r"C:\Users\Roy.DEV\Desktop\duck.ppm"
# image1 = Image.open(file)
# image1.thumbnail((50, 50), Image.ANTIALIAS)
# img = ImageTk.PhotoImage(image1)
img = tk.PhotoImage(file=file1)
rtm_image = tk.Label(frame, image=img)

rtm_image.place(relx=.5, rely=.5, anchor="center")

root.mainloop()