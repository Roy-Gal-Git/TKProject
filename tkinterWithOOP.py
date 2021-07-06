import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image

LARGE_FONT = ("Ariel", 12)
WINDOW_WIDTH = 410
WINDOW_HEIGHT = 230


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
        label.pack(fill="both", expand=True)

    except:
        window.destroy()


# This class acts as the main WINDOW and hosts many frames inside it - a controller that has methods that every frame
# it hosts can use to go get around the application's pages
class ContainerFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)
        self.geometry(self.top_center_screen())
        self.title("TKProject")
        self.container.pack(side='top', fill='both', expand=True)
        self.users_info = {"Roy": "Aa123456", "": ""}

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.pages = [HomePage, PageOne, PageTwo, PageThree]

        for F in self.pages:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    # Raises the given frame (wanted_frame argument) above the others that are hosted on the container frame
    def show_frame(self, wanted_frame):
        frame = self.frames[wanted_frame]
        frame.tkraise()

    # Finds the middle-top spot on a screen and returns it as a value usable in a .geometry() method
    def top_center_screen(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        y = int((screen_height / 2) - (WINDOW_HEIGHT / 2)) - 200
        return '{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, x, y)

    # Checks if the inputted username and password match the ones in the username-password pool (users_info dict)
    def verify(self, un, pw):
        verified = False
        for U in self.users_info.items():
            if U[0] == un and U[1] == pw:
                verified = True
        if verified:
            self.show_frame(PageOne)
            self.frames[HomePage].destroy()
        else:
            messagebox.showerror(title="Error!", message="Login Failed!")

    # Creates a new HomePage frame since it was destroyed for sure before this method was used
    # (It creates it from scratch so after you pass the home page the details a user inputted in
    # the entries would be cleared off them.
    def go_to_homepage(self):
        frame = HomePage(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")

    # Creates a new Register frame since it was destroyed for sure before this method was used
    # (It creates it from scratch so after you pass the register page the details a user inputted in
    # the entries would be cleared off them.
    def go_to_register(self):
        frame = Register(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[HomePage].destroy()

    # Adds the inputs from the entries to the username-password pool (users_info dict)
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

    # Creates a brand new window (not a frame) that's stacked on the root window.
    def create_new_window(self):
        # TK Window
        new_window = tk.Toplevel(self)
        new_window.geometry(self.top_center_screen())
        new_window.config(bg="black")

        # Frames
        top_frame = tk.Frame(new_window, bg="red")
        top_frame.pack(side="top", anchor="n", expand=True, fill="x")

        top_n_frame = tk.Frame(top_frame, bg="orange")
        top_n_frame.pack(side="top", anchor="n", expand=True, fill="x")

        top_nwne_frame = tk.Frame(top_frame, bg="orange")
        top_nwne_frame.pack(side="top", anchor="center", expand=True, fill="both")

        bottom_frame = tk.Frame(new_window, bg="blue")
        bottom_frame.pack(side="bottom", anchor="s", expand=True, fill="x")

        bottom_s_frame = tk.Frame(bottom_frame, bg="pink")
        bottom_s_frame.pack(side="bottom", anchor="s", expand=True, fill="x")

        bottom_swse_frame = tk.Frame(bottom_frame, bg="pink")
        bottom_swse_frame.pack(side="bottom", anchor="s", expand=True, fill="both")

        right_frame = tk.Frame(new_window, bg="green")
        right_frame.pack(side="right", anchor="e")

        left_frame = tk.Frame(new_window, bg="green")
        left_frame.pack(side="left", anchor="w")

        # Buttons
        n_button = ttk.Button(top_n_frame, text="N",
                              command=lambda: self.set_button_by_direction(new_window, "top", "n"))
        n_button.pack(padx=2, pady=2, side="top", anchor="n")

        s_button = ttk.Button(bottom_s_frame, text="S",
                              command=lambda: self.set_button_by_direction(new_window, "bottom", "s"))
        s_button.pack(padx=2, pady=2, side="bottom", anchor="s")

        w_button = ttk.Button(left_frame, text="W",
                              command=lambda: self.set_button_by_direction(new_window, "left", "w"))
        w_button.pack(padx=2, pady=2, side="left", anchor="w")

        nw_button = ttk.Button(top_nwne_frame, text="NW",
                               command=lambda: self.set_button_by_direction(new_window, "left", "nw"))
        nw_button.pack(padx=2, pady=2, side="left", anchor="nw")

        sw_button = ttk.Button(bottom_swse_frame, text="SW",
                               command=lambda: self.set_button_by_direction(new_window, "left", "sw"))
        sw_button.pack(padx=2, pady=2, side="left", anchor="sw")

        e_button = ttk.Button(right_frame, text="E",
                              command=lambda: self.set_button_by_direction(new_window, "right", "e"))
        e_button.pack(padx=2, pady=2, side="right", anchor="e")

        ne_button = ttk.Button(top_nwne_frame, text="NE",
                               command=lambda: self.set_button_by_direction(new_window, "right", "ne"))
        ne_button.pack(padx=2, pady=2, side="right", anchor="ne")

        se_button = ttk.Button(bottom_swse_frame, text="SE",
                               command=lambda: self.set_button_by_direction(new_window, "right", "se"))
        se_button.pack(padx=2, pady=2, side="right", anchor="se")

    # Setting the button in the creation page to the same direction of the buttons in the new pop-up window
    def set_button_by_direction(self, new_window, side, anchor):
        self.frames[PageThree].creation_command(self)
        self.frames[PageCreation].button = None

        # Logic behind where should the buttons be created
        if anchor == "nw":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].nw_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))
        if anchor == "n":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].n_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        if anchor == "ne":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].ne_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        if anchor == "w":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].w_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        if anchor == "e":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].e_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        if anchor == "sw":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].sw_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        if anchor == "s":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].s_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        if anchor == "se":
            self.frames[PageCreation].button = ttk.Button(self.frames[PageCreation].se_frame, text="Prev",
                                                          command=lambda: self.frames[PageCreation].show_prev_page(self))

        self.frames[PageCreation].button.pack(padx=2, pady=2, side=side, anchor=anchor)

        new_window.destroy()


# This class represents the Register frame
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


# This class represents the HomePage frame
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


# This class represents the PageOne frame
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


# This class represents the PageTwo frame
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.menu_frame = tk.Frame(self, bg="cyan")
        self.menu_frame.pack(fill="y", side="left", anchor="w")

        menu_label = ttk.Label(self.menu_frame, text="Menu:", background="white", font=LARGE_FONT)
        menu_label.pack(padx=20, pady=20)

        self.buttons_frame = tk.Frame(self.menu_frame)
        self.buttons_frame.pack(side="bottom", anchor="w")

        self.prev_button_frame = tk.Frame(self.buttons_frame, bg="cyan")
        self.prev_button_frame.pack(side="left", anchor="w")

        self.next_button_frame = tk.Frame(self.buttons_frame, bg="cyan")
        self.next_button_frame.pack(side="right", anchor="w")

        menu_prev_button = ttk.Button(self.prev_button_frame, text="Prev",
                                      command=lambda: controller.show_frame(PageOne))
        menu_prev_button.pack(padx=2, pady=2, side="bottom", anchor="sw")

        menu_next_button = ttk.Button(self.next_button_frame, text="Next",
                                      command=lambda: controller.show_frame(PageThree))
        menu_next_button.pack(padx=2, pady=2, side="bottom", anchor="se")

        self.right_container = tk.Frame(self, bg="medium aquamarine")
        self.right_container.pack(fill="both", side="top", anchor="s", expand=True)

        # Right top container
        self.rt_container = tk.Frame(self.right_container)
        self.rt_container.pack(fill="both", expand=True)

        # Right top left
        self.rtl_frame = tk.Frame(self.rt_container, bg="dark turquoise")
        self.rtl_frame.pack(side="left", anchor="nw", fill="both", expand=True)

        rtl_label = ttk.Label(self.rtl_frame, text="LEFT", font=LARGE_FONT, background="white")
        rtl_label.pack(padx=20, pady=20, anchor="n")

        # Right top middle
        self.rtm_frame = tk.Frame(self.rt_container, bg="steel blue")
        self.rtm_frame.pack(side="left", anchor="n", fill="both", expand=True)

        rtm_label = ttk.Label(self.rtm_frame, text="MID", font=LARGE_FONT, background="white")
        rtm_label.pack(padx=20, pady=20, anchor="n")

        # Right top right
        self.rtr_frame = tk.Frame(self.rt_container, bg="dark sea green")
        self.rtr_frame.pack(side="left", anchor="ne", fill="both", expand=True)

        rtr_label = ttk.Label(self.rtr_frame, text="RIGHT", font=LARGE_FONT, background="white")
        rtr_label.pack(padx=20, pady=20, anchor="n")

        # Right bottom
        self.rb_frame = tk.Frame(self.right_container, bg="royal blue")
        self.rb_frame.pack(side="bottom", anchor="s", fill="both", expand=True)

        rb_label = ttk.Label(self.rb_frame, text="BOTTOM", font=LARGE_FONT, background="white")
        rb_label.pack(padx=20, pady=20, anchor="n")


# This class represents the PageThree frame
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.next_button_exists = False
        self.p3_next_button = None

        p3_label = ttk.Label(self, text="CREATION", font=LARGE_FONT, background="steelblue")
        p3_label.pack(padx=20, pady=20)

        create_button = ttk.Button(self, text="Create Button",
                                   command=lambda: controller.create_new_window())
        create_button.pack(padx=2, pady=2, side='top', anchor='center')

        p3_prev_button = ttk.Button(self, text="Prev",
                                    command=lambda: self.show_prev_page(controller))
        p3_prev_button.pack(padx=2, pady=2, side="left", anchor="sw")

    # A method that creates the next button on the PageThree frame and adds a new frame into the frames dictionary.
    # It also creates that new frame and lowers it so the PageThree frame would still be displayed.
    def creation_command(self, controller):
        if not self.next_button_exists:
            self.next_button_exists = True

            # Creating the new page
            frame = PageCreation(controller.container, controller)
            controller.frames[PageCreation] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            frame.lower()

            self.p3_next_button = ttk.Button(self, text="Next",
                                             command=lambda: controller.show_frame(PageCreation))
            self.p3_next_button.pack(padx=2, pady=2, side="right", anchor="se")

    # Deletes the creation page and page 3's next button if it exists
    def show_prev_page(self, controller):
        if PageCreation in controller.frames:
            del controller.frames[PageCreation]
        if self.next_button_exists:
            self.p3_next_button.destroy()
            self.next_button_exists = False
        controller.show_frame(PageTwo)


# This class represents the PageCreation frame
class PageCreation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.prev_page = controller.frames[PageThree]

        pc_label = ttk.Label(self, text="Creation Page", font=LARGE_FONT, background="magenta")
        pc_label.pack(padx=20, pady=20)

        # Scalable main frame that holds everything
        self.scalable_frame = tk.Frame(self)
        self.scalable_frame.pack()

        self.scalable_frame.grid_rowconfigure(0, weight=1)
        self.scalable_frame.grid_columnconfigure(0, weight=1)
        self.scalable_frame.grid_rowconfigure(1, weight=1)
        self.scalable_frame.grid_columnconfigure(1, weight=1)
        self.scalable_frame.grid_rowconfigure(2, weight=1)
        self.scalable_frame.grid_columnconfigure(2, weight=1)

        # Inner frames added with grid into the scalable frame
        self.nw_frame = tk.Frame(self.scalable_frame, bg="gold")
        self.nw_frame.grid(row=0, column=0, sticky="nsew", ipadx=60, ipady=25)
        self.nw_frame.pack_propagate(0)

        self.n_frame = tk.Frame(self.scalable_frame, bg="spring green")
        self.n_frame.grid(row=0, column=1, sticky="nsew", ipadx=60, ipady=25)
        self.n_frame.pack_propagate(0)

        self.ne_frame = tk.Frame(self.scalable_frame, bg="cyan")
        self.ne_frame.grid(row=0, column=2, sticky="nsew", ipadx=60, ipady=25)
        self.ne_frame.pack_propagate(0)

        self.w_frame = tk.Frame(self.scalable_frame, bg="yellow")
        self.w_frame.grid(row=1, column=0, sticky="nsew", ipadx=60, ipady=25)
        self.w_frame.pack_propagate(0)

        self.center_frame = tk.Frame(self.scalable_frame, bg="peach puff")
        self.center_frame.grid(row=1, column=1, sticky="nsew", ipadx=60, ipady=25)
        self.center_frame.pack_propagate(0)

        self.e_frame = tk.Frame(self.scalable_frame, bg="red")
        self.e_frame.grid(row=1, column=2, sticky="nsew", ipadx=60, ipady=25)
        self.e_frame.pack_propagate(0)

        self.sw_frame = tk.Frame(self.scalable_frame, bg="VioletRed2")
        self.sw_frame.grid(row=2, column=0, sticky="nsew", ipadx=60, ipady=25)
        self.sw_frame.pack_propagate(0)

        self.s_frame = tk.Frame(self.scalable_frame, bg="chocolate1")
        self.s_frame.grid(row=2, column=1, sticky="nsew", ipadx=60, ipady=25)
        self.s_frame.pack_propagate(0)

        self.se_frame = tk.Frame(self.scalable_frame, bg="royal blue")
        self.se_frame.grid(row=2, column=2, sticky="nsew", ipadx=60, ipady=25)
        self.se_frame.pack_propagate(0)

    # Deletes the PageCreation frame and the PageThree frame's next button since it exists for sure now
    def show_prev_page(self, controller):
        controller.frames[PageCreation].destroy()
        if PageCreation in controller.frames:
            del controller.frames[PageCreation]
        if self.prev_page.next_button_exists:
            self.prev_page.p3_next_button.destroy()
            self.prev_page.next_button_exists = False
        controller.show_frame(PageThree)


def main():
    parent_window = ContainerFrame()
    parent_window.mainloop()


if __name__ == '__main__':
    main()
