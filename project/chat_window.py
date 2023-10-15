import ttkbootstrap as ttk


class ChatWindow:
    def __init__(self, parent=None):
        # self.master = parent

        # self.root = ttk.Toplevel()
        self.root = ttk.Window(themename='morph')

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 650) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 650) // 2

        self.root.geometry(f'650x650+{x_position}+{y_position}')
        self.root.minsize(500, 550)


# chat = ChatWindow()
# chat.root.mainloop()
