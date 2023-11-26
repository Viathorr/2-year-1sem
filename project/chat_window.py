import socket
import threading
import rsa
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from datetime import datetime
from tkinter import messagebox

PORT = 9999
SERVER = '192.168.95.126'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


class ChatWindow:
    def __init__(self, parent):
        self.master = parent.master
        self.parent = parent

        self.root = ttk.Toplevel(title='Chat')
        self.root.iconbitmap('rsrc/chat.ico')
        self.root.minsize(650, 650)
        self.root.bind('<Configure>', lambda event: self.resize())
        # self.root.resizable(False, False)

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 650) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 650) // 2

        self.root.geometry(f'650x650+{x_position}+{y_position - 30}')

        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=4)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=2)

        btn_style = ttk.Style()
        btn_style.configure(style='TButton', font=('Microsoft JhengHei Light', 10, 'bold'))

        # Label that represents amount of participants in chat
        self.num_of_participants = ttk.StringVar(value='Participants: 1')
        self.participants_label = ttk.Label(self.root, textvariable=self.num_of_participants, cursor='hand2',
                                            font=('Microsoft JhengHei', 13, 'bold'), bootstyle='info')
        self.participants_label.grid(row=0, column=0, columnspan=2, pady=7, padx=7, sticky='nw')
        ToolTip(self.participants_label, 'Show all participants', bootstyle='secondary-inverse')

        # Textbox to display messages (temporary)
        self.text_widget = ttk.Text(self.root, state=DISABLED, height=20, width=self.root.winfo_width(),
                                    font=('Microsoft JhengHei Light', 10, 'bold'), foreground='black')
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
        self.send_msg_btn = ttk.Button(self.root, text='Send', command=lambda: self._send_message(), width=10,
                                  bootstyle='info')
        self.send_msg_btn.grid(row=2, column=1, padx=10, pady=5, sticky='w', ipady=4)

    def open(self):
        self.root.mainloop()

    def resize(self):
        self.participants_label.config(font=('Microsoft JhengHei', int((13*self.root.winfo_height())/650), 'bold'))
        self.msg_entry.config(width=int((45*self.root.winfo_width())/650))
        self.send_msg_btn.config(width=int((10*self.root.winfo_width())/650))
        self.text_widget.config(height=((21*self.root.winfo_height())/650))

    def _scrollbar_appearing(self):
        self.scrollbar = ttk.Scrollbar(self.text_widget, bootstyle='secondary-round', command=self.text_widget.yview)
        self.scrollbar.place(relheight=1, relx=0.975)

        self.text_widget.config(yscrollcommand=self.scrollbar.set)

    def _scrollbar_disappearing(self):
        self.scrollbar.place_forget()

    def _send_message(self):
        if not self.msg_entry.get():
            return
        elif self.msg_entry.get() == "Message":
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


class ClientChatWindow(ChatWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connected = False
        self._public_key = None
        self._private_key = None
        self._server_public_key = None
        self._participants = []

        self.participants_label.bind('<Button-1>', lambda event: self._open_list_of_participants())

    def open(self):
        self._connect()

    def _connect(self):
        try:
            self.socket.connect(ADDR)
            self._connected = True
            self._generate_keys()
            self._server_public_key = rsa.PublicKey.load_pkcs1(self.socket.recv(1024))
            self.socket.send(rsa.PublicKey.save_pkcs1(self._public_key))
            msg = rsa.decrypt(self.socket.recv(1024), self._private_key).decode(FORMAT)
            if msg == 'NICK':
                self.socket.send(rsa.encrypt(self.master.user.name.encode(FORMAT), self._server_public_key))
            thread_receive = threading.Thread(target=self._receive)
            thread_receive.start()
            self.root.mainloop()
        except socket.error:
            raise Exception('Failed to connect to server! Try again.')

    def _send_message(self):
        if not self.msg_entry.get() or self.msg_entry.get() == "Message":
            return
        else:
            curr_time = datetime.now().time()
            time = curr_time.strftime('%H:%M')
            message = f'{self.master.user.name}: {self.msg_entry.get()}\n{time}\n\n'
            self.socket.send(rsa.encrypt(message.encode(FORMAT), self._server_public_key))
            self.msg_entry.delete(0, END)

    def _receive(self):
        while True:
            try:
                msg = rsa.decrypt(self.socket.recv(1024), self._private_key).decode(FORMAT)
                if msg.startswith('PARTICIPANTS'):
                    self._participants.clear()
                    lines = msg.split('\n')
                    for i in range(1, len(lines)):
                        nickname = lines[i]
                        self._participants.append(nickname)
                    self.num_of_participants.set(f'Participants: {len(self._participants)}')
                else:
                    self.text_widget.config(state=NORMAL)
                    self.text_widget.insert(END, msg)
                    self.text_widget.see(END)
                    self.text_widget.config(state=DISABLED)
            except socket.error:
                if self.socket.fileno() == -1:
                    break
                self.socket.close()
                self.root.destroy()
                self.parent.root.deiconify()
                messagebox.showerror(title='Error', message="Server doesn't answer. Please try again.")
                break

    def _open_list_of_participants(self):
        participants_list = ttk.Toplevel(title='Participants')
        participants_list.iconbitmap('rsrc/chat.ico')

        x_position = (self.root.winfo_screenwidth() - 350) // 2
        y_position = (self.root.winfo_screenheight() - 400) // 2

        participants_list.geometry(f'350x400+{x_position}+{y_position - 30}')
        participants_list.minsize(350, 400)

        my_list = tk.Listbox(participants_list, font=('Microsoft JhengHei Light', 10), foreground='black',
                             selectborderwidth=1)
        my_list.pack(padx=5, pady=5, fill='both', expand=True)

        for nick in self._participants:
            my_list.insert(END, nick)

        participants_list.mainloop()

    def _generate_keys(self):
        self._public_key, self._private_key = rsa.newkeys(1024)

    def close(self):
        self.socket.close()
