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
        self.root.minsize(650, 650)

        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=6)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=5)
        self.root.columnconfigure(1, weight=1)

        # Label that represents amount of participants in chat
        self.num_of_participants = ttk.StringVar(value='Number of participants: 1')
        self.participants_label = ttk.Label(self.root, textvariable=self.num_of_participants, cursor='hand2',
                                            font=('Microsoft JhengHei Light', 16, 'bold'))
        self.participants_label.bind('<FocusIn>', lambda event: self.open_list_of_participants())
        self.participants_label.grid(row=0, column=0, columnspan=2, pady=5, sticky='nw')

        # Textbox to display messages (temporary)
        self.chat

    def open(self):
        self.root.mainloop()

    def open_list_of_participants(self):
        pass


if __name__ == '__main__':
    check = ChatWindow()
    check.open()
