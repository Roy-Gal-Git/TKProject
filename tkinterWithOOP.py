import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk
# import numpy as np


LARGE_FONT = ("Ariel", 12)
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200

# Uses the file explorer to choose a picture and display it in a new window
def browse_files():
    try:
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("JPEG", "*.JPG*"), ("all files", "*.*")))
        window = tk.Tk()
        window.title("")
        test = ImageTk.PhotoImage(master=window, file=filename)
        label = tk.Label(window, image=test)
        label.image = test
        label.grid(row=0, column=0, sticky="nsew")

    except:
        window.destroy()


# This class acts as the main WINDOW and hosts many frames inside it - a controller that has methods that every frame
# it hosts can use to go get around the application's pages
class ContainerFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.geometry(self.top_center_screen())
        self.title("TKProject")
        self.container.pack(side='top', fill='both', expand=True)
        self.users_info = {"Roy": "Aa123456"}

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.pages = [HomePage, PageOne, PageTwo]
        # self.pages = np.array([HomePage, PageOne, PageTwo])
        # self.counter = 0

        for F in self.pages:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, wanted_frame):
        frame = self.frames[wanted_frame]
        frame.tkraise()

    def top_center_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        y = int((screen_height / 2) - (WINDOW_HEIGHT / 2)) - 200
        return '{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, x, y)

    # def next_page(self):
    #     self.counter += 1
    #     self.show_frame(self.pages[self.counter])
    #
    # def prev_page(self):
    #     self.counter -= 1
    #     self.show_frame(self.pages[self.counter])

    def verify(self, un, pw):
        flag = False
        for U in self.users_info.items():
            if U[0] == un and U[1] == pw:
                flag = True
        if flag:
            self.show_frame(PageOne)
            self.frames[HomePage].destroy()
        else:
            messagebox.showerror(title="Error!", message="Login Failed!")

    def go_to_homepage(self):
        frame = HomePage(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")

    def go_to_register(self):
        frame = Register(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[HomePage].destroy()

    def register(self, un, pw1, pw2):
        if pw1 == pw2 and pw1 != "" and un != "":
            if un in self.users_info:
                messagebox.showerror(title="Error!", message="User Already Exists!")
            else:
                self.users_info[un] = pw1
                messagebox.showinfo(title="Notice", message="Registration Complete!")
        elif pw1 == "" or pw2 == "" or un == "":
            messagebox.showerror(title="Error!", message="Missing Details!")
        else:
            messagebox.showerror(title="Error!", message="Passwords Don't Match!")


class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frame1 = tk.Frame(self)
        self.frame1.pack()
        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        label = ttk.Label(self.frame1, text="Register:", font=LARGE_FONT, background="white")
        label.grid(row=0, column=1, pady=20, padx=20)

        username_label = ttk.Label(self.frame2, text="Username:", font=LARGE_FONT)
        username_label.grid(row=1, column=0, padx=10, pady=2)

        username_entry = ttk.Entry(self.frame2)
        username_entry.grid(row=1, column=1, padx=10, pady=2)

        password1_label = ttk.Label(self.frame2, text="Password:", font=LARGE_FONT)
        password1_label.grid(row=2, column=0, padx=10, pady=2)

        password1_entry = ttk.Entry(self.frame2, show="*")
        password1_entry.grid(row=2, column=1, padx=10, pady=2)

        password2_label = ttk.Label(self.frame2, text="Verify:", font=LARGE_FONT)
        password2_label.grid(row=3, column=0, padx=10, pady=2)

        password2_entry = ttk.Entry(self.frame2, show="*")
        password2_entry.grid(row=3, column=1, padx=10, pady=2)

        home_button = ttk.Button(self.frame2, text="Home", width=10,
                                 command=lambda: controller.go_to_homepage())
        home_button.grid(row=4, column=1, pady=2, sticky="w")

        register_button = ttk.Button(self.frame2, text="Register", width=10,
                                     command=lambda: controller.register(username_entry.get(),
                                                                         password1_entry.get(),
                                                                         password2_entry.get()))
        register_button.grid(row=4, column=1, pady=2, sticky="e")


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frame1 = tk.Frame(self)
        self.frame1.pack()
        self.frame2 = tk.Frame(self)
        self.frame2.pack()
        label = ttk.Label(self.frame1, text="Home Page", font=LARGE_FONT, background="pink")
        label.grid(row=0, column=1, pady=20, padx=20)

        username_label = ttk.Label(self.frame2, text="Username:", font=LARGE_FONT)
        username_label.grid(row=1, column=0, padx=10, pady=2)

        username_entry = ttk.Entry(self.frame2)
        username_entry.grid(row=1, column=1, padx=10, pady=2)

        password_label = ttk.Label(self.frame2, text="Password:", font=LARGE_FONT)
        password_label.grid(row=2, column=0, padx=10, pady=2)

        password_entry = ttk.Entry(self.frame2, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=2)

        login_button = ttk.Button(self.frame2, text="Login", width=10,
                                  command=lambda: controller.verify(username_entry.get(), password_entry.get()))
        login_button.grid(row=3, column=1, pady=2, sticky="e")

        register_button = ttk.Button(self.frame2, text="Register", width=10,
                                     command=lambda: controller.go_to_register())
        register_button.grid(row=3, column=1, pady=2, sticky="w")


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        p1_label = ttk.Label(self, text="Page One", font=LARGE_FONT, background="red")
        p1_label.pack(padx=20, pady=20)

        p1_prev_button = ttk.Button(self, text="Logout",
                                    command=lambda: controller.go_to_homepage())
        p1_prev_button.pack(padx=2, pady=2, side="left", anchor="sw")

        p1_next_button = ttk.Button(self, text="Next",
                                    command=lambda: controller.show_frame(PageTwo))
        p1_next_button.pack(padx=2, pady=2, side="right", anchor="se")

        p1_browse_button = ttk.Button(self, text="Browse",
                                      command=lambda: browse_files())
        p1_browse_button.pack(padx=2, pady=2, side='top', anchor='center')


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        p2_label = ttk.Label(self, text="Page Two", font=LARGE_FONT, background="cyan")
        p2_label.pack(padx=20, pady=20)

        p2_prev_button = ttk.Button(self, text="Prev",
                                    command=lambda: controller.show_frame(PageOne))
        p2_prev_button.pack(padx=2, pady=2, side="bottom", anchor="sw")


app = ContainerFrame()
app.mainloop()
