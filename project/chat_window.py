import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip


class ChatWindow:
    def __init__(self, parent=None):
        self.master = parent.master

        self.root = ttk.Toplevel()
        # self.root = ttk.Window(themename='morph')

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 650) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 650) // 2

        self.root.geometry(f'650x650+{x_position}+{y_position}')
        self.root.minsize(650, 650)

        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=4)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=2)

        btn_style = ttk.Style()
        btn_style.configure(style='TButton', font=('Microsoft JhengHei Light', 10, 'bold'))

        # Label that represents amount of participants in chat
        self.num_of_participants = ttk.StringVar(value='Number of participants: 1')
        participants_label = ttk.Label(self.root, textvariable=self.num_of_participants, cursor='hand2',
                                       font=('Microsoft JhengHei Light', 13, 'bold'), bootstyle='info')
        participants_label.bind('<FocusIn>', lambda event: self.open_list_of_participants())
        participants_label.grid(row=0, column=0, columnspan=2, pady=7, padx=7, sticky='nw')
        ToolTip(participants_label, 'Show all participants', bootstyle='secondary-inverse')

        # Textbox to display messages (temporary)
        self.text_widget = ttk.Text(self.root, state=DISABLED, height=20, font=('Microsoft JhengHei Light', 10, 'bold'),
                                    foreground='black')
        self.text_widget.grid(row=1, columnspan=2, padx=4)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.text_widget, bootstyle='secondary-round', command=self.text_widget.yview)
        scrollbar.place(relheight=1, relx=0.975)

        self.text_widget.config(yscrollcommand=scrollbar.set)

        # Message entry
        self.msg_entry = ttk.Entry(self.root, width=45, foreground='black', font=('Microsoft JhengHei Light', 10))
        self.msg_entry.grid(row=2, column=0, sticky='w', padx=4, pady=14, ipady=5)
        self.msg_entry.bind('<Return>', lambda event: self._send_message())

        # Enter button
        send_msg_btn = ttk.Button(self.root, text='Send', command=lambda: self._send_message(), width=10,
                                  bootstyle='info')
        send_msg_btn.grid(row=2, column=1, padx=10, pady=5, sticky='w', ipady=4)

    def open(self):
        self.root.mainloop()

    def _send_message(self):
        if not self.msg_entry.get():
            return
        else:
            message = f'{self.master.user.name}: {self.msg_entry.get()}\n\n'
            self.text_widget.config(state=NORMAL)
            self.text_widget.insert(END, message)
            self.text_widget.config(state=DISABLED)
            self.msg_entry.delete(0, END)

    def open_list_of_participants(self):
        pass


if __name__ == '__main__':
    check = ChatWindow()
    check.open()
