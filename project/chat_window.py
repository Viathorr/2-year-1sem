import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from datetime import datetime


class ChatWindow:
    def __init__(self, parent):
        self.master = parent.master

        self.root = ttk.Toplevel()
        # self.root = ttk.Window(title='Chat')
        self.root.iconbitmap('rsrc/chat.ico')

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 650) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 650) // 2

        self.root.geometry(f'650x650+{x_position}+{y_position-30}')
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
        participants_label.bind('<Button-1>', lambda event: self.open_list_of_participants())
        participants_label.grid(row=0, column=0, columnspan=2, pady=7, padx=7, sticky='nw')
        ToolTip(participants_label, 'Show all participants', bootstyle='secondary-inverse')

        # Textbox to display messages (temporary)
        self.text_widget = ttk.Text(self.root, state=DISABLED, height=20, font=('Microsoft JhengHei Light', 10, 'bold'),
                                    foreground='black')
        self.text_widget.grid(row=1, columnspan=2, padx=4)
        self.text_widget.bind('<Enter>', lambda event: self._scrollbar_appearing())
        self.text_widget.bind('<Leave>', lambda event: self._scrollbar_disappearing())
        # Scrollbar for text widget
        self.scrollbar = None

        # Message entry
        self.msg_entry = ttk.Entry(self.root, width=45, foreground='gray', font=('Microsoft JhengHei Light', 10))
        self.msg_entry.insert(0, 'Message')
        self.msg_entry.grid(row=2, column=0, sticky='w', padx=10, pady=14, ipady=5)
        self.msg_entry.bind('<Return>', lambda event: self._send_message())
        self.msg_entry.bind('<FocusIn>', lambda event: self._delete_default_text())
        self.msg_entry.bind('<FocusOut>', lambda event: self._set_default_text())

        # Enter button
        send_msg_btn = ttk.Button(self.root, text='Send', command=lambda: self._send_message(), width=10,
                                  bootstyle='info')
        send_msg_btn.grid(row=2, column=1, padx=10, pady=5, sticky='w', ipady=4)

    def open(self):
        self.root.mainloop()

    def _scrollbar_appearing(self):
        self.scrollbar = ttk.Scrollbar(self.text_widget, bootstyle='secondary-round', command=self.text_widget.yview)
        self.scrollbar.place(relheight=1, relx=0.975)

        self.text_widget.config(yscrollcommand=self.scrollbar.set)

    def _scrollbar_disappearing(self):
        self.scrollbar.place_forget()

    def _send_message(self):
        if not self.msg_entry.get():
            return
        else:
            curr_time = datetime.now().time()
            time = curr_time.strftime('%H:%M')
            message = f'{self.master.user.name}: {self.msg_entry.get()}\n{time}\n\n'
            self.text_widget.config(state=NORMAL)
            self.text_widget.insert(END, message)
            self.text_widget.see(END)
            self.text_widget.config(state=DISABLED)
            self.msg_entry.delete(0, END)
            self.root.focus_set()
            self._set_default_text()

    def _set_default_text(self):
        if self.msg_entry.get() == '':
            self.msg_entry.config(foreground='gray')
            self.msg_entry.insert(0, 'Message')

    def _delete_default_text(self):
        if self.msg_entry.get() == 'Message':
            self.msg_entry.delete(0, END)
            self.msg_entry.config(foreground='black')

    def open_list_of_participants(self):
        participants_list = ttk.Toplevel(title='Participants')
        participants_list.iconbitmap('rsrc/chat.ico')

        x_position = (self.root.winfo_screenwidth() - 350) // 2
        y_position = (self.root.winfo_screenheight() - 400) // 2

        participants_list.geometry(f'350x400+{x_position}+{y_position - 30}')
        participants_list.minsize(350, 400)

        my_list = tk.Listbox(participants_list, font=('Microsoft JhengHei Light', 10), foreground='black',
                             selectborderwidth=1)
        my_list.pack(padx=5, pady=5, fill='both', expand=True)
        my_list.insert(END, self.master.user.name)
        participants_list.mainloop()


if __name__ == '__main__':
    check = ChatWindow()
    check.open()
