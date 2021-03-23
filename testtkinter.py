import tkinter as tk
from tkinter import ttk

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 250

root = tk.Tk()


def center_screen():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
    y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))
    return '{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, x, y)


def get_x():
    screen_width = root.winfo_screenwidth()
    x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
    return x


def get_y():
    screen_height = root.winfo_screenheight()
    y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))
    return y


root['bg'] = 'red'
root.geometry(center_screen())
frame = tk.Frame(root, bg='pink')
frame.pack(expand=1, fill='both')

menu_text = tk.Label(frame, text="Main Menu", fg='black', bg='yellow')
menu_text.pack(pady=20)

button_next = tk.Button(frame, text="Next", fg='black', bg='blue')
button_next.pack(padx=20, pady=20, side='bottom', anchor='e')


root.mainloop()