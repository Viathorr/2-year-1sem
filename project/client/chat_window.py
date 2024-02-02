import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from datetime import datetime
from tkinter import messagebox
from abc import ABC, abstractmethod
from client.client_socket.client_socket import ClientSocket


class ChatWindow(ABC):
    """
    Class for the sign-up window.

    Attributes:
        _master (ChatApp): The application object.
        root (ttk.Toplevel): Toplevel window with Signup form.
        _num_of_participants (ttk.StringVar): Value of participants label.
        _participants_label (ttk.Label): Label that shows the amount of participants.
        _text_widget (ttk.Text): Text widget that display all the messages.
        _msg_entry (ttk.Entry): Message entry field to write messages.
        _send_msg_btn (ttk.Button): The button to login.

    Methods:
        open(self):
            Opens the signup window.
        _delete_default_text(num: int):
            Deletes the default text in the message entry field.
        _set_default_text(num: int):
            Sets the default text in the message entry field.
        _send_message():
            Sends a message (displays on the text widget).
        resize():
            Resizes all window components according to the size of window.
        _scrollbar_appearing():
            Handles the appearance of scrollbar everytime the text widget is focused.
        _scrollbar_disappearing():
            Handles the disappearance of scrollbar everytime the text widget is out of focus.

    """
    def __init__(self, master) -> None:
        """
        Initialize the chat window.

        Args:
            master (ChatApp): The application object.
        """
        self._master = master

        self.root = ttk.Toplevel(title='Chat')
        self.root.iconbitmap('./rsrc/chat.ico')
        self.root.minsize(650, 650)
        self.root.bind('<Configure>', lambda event: self._resize())
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
        self._num_of_participants = ttk.StringVar(value='Participants: 1')
        self._participants_label = ttk.Label(self.root, textvariable=self._num_of_participants, cursor='hand2',
                                             font=('Microsoft JhengHei', 13, 'bold'), bootstyle='info')
        self._participants_label.grid(row=0, column=0, columnspan=2, pady=7, padx=7, sticky='nw')
        ToolTip(self._participants_label, 'Show all participants', bootstyle='secondary-inverse')

        # Textbox to display messages (temporary)
        self._text_widget = ttk.Text(self.root, state=DISABLED, height=20, width=self.root.winfo_width(),
                                     font=('Microsoft JhengHei Light', 10, 'bold'), foreground='black')
        self._text_widget.grid(row=1, columnspan=2, padx=4)
        self._text_widget.bind('<Enter>', lambda event: self._scrollbar_appearing())
        self._text_widget.bind('<Leave>', lambda event: self._scrollbar_disappearing())
        # Scrollbar for text widget
        self._scrollbar = None

        # Message entry
        self._msg_entry = ttk.Entry(self.root, width=45, foreground='gray', font=('Microsoft JhengHei Light', 10))
        self._msg_entry.insert(0, 'Message')
        self._msg_entry.grid(row=2, column=0, sticky='w', padx=10, pady=14, ipady=5)
        self._msg_entry.bind('<Return>', lambda event: self._send_message())
        self._msg_entry.bind('<FocusIn>', lambda event: self._delete_default_text())
        self._msg_entry.bind('<FocusOut>', lambda event: self._set_default_text())
        ToolTip(self._msg_entry, 'Message limit: 95 characters', bootstyle='info-inverse')

        # Enter button
        self._send_msg_btn = ttk.Button(self.root, text='Send', command=lambda: self._send_message(), width=10,
                                        bootstyle='info')
        self._send_msg_btn.grid(row=2, column=1, padx=10, pady=5, sticky='w', ipady=4)

    def open(self) -> None:
        """
        Open the chat window.
        """
        self.root.mainloop()

    def _resize(self) -> None:
        """
        Resize all window components according to the size of window.
        """
        self._participants_label.config(font=('Microsoft JhengHei', int((13 * self.root.winfo_height()) / 650), 'bold'))
        self._msg_entry.config(width=int((45 * self.root.winfo_width()) / 650))
        self._send_msg_btn.config(width=int((10 * self.root.winfo_width()) / 650))
        self._text_widget.config(height=((21 * self.root.winfo_height()) / 650))

    def _scrollbar_appearing(self) -> None:
        """
        Handle the appearance of scrollbar everytime the text widget is focused.
        """
        self._scrollbar = ttk.Scrollbar(self._text_widget, bootstyle='secondary-round', command=self._text_widget.yview)
        self._scrollbar.place(relheight=1, relx=0.975)

        self._text_widget.config(yscrollcommand=self._scrollbar.set)

    def _scrollbar_disappearing(self) -> None:
        """
        Handle the disappearance of scrollbar everytime the text widget is out of focus.
        """
        self._scrollbar.place_forget()

    def _send_message(self) -> None:
        """
        Send a message (display on the text widget).
        """
        if self._msg_entry.get() and self._msg_entry.get() != "Message":
            curr_time = datetime.now().time()
            time = curr_time.strftime('%H:%M')
            message = f'{self._master.user.name}: {self._msg_entry.get()}\n{time}\n\n'
            self._text_widget.config(state=NORMAL)
            self._text_widget.insert(END, message)
            self._text_widget.see(END)
            self._text_widget.config(state=DISABLED)
            self._msg_entry.delete(0, END)
            self.root.focus_set()
            self._set_default_text()

    def _set_default_text(self) -> None:
        """
        Set the default text in the entry field.
        """
        if self._msg_entry.get() == '':
            self._msg_entry.config(foreground='gray')
            self._msg_entry.insert(0, 'Message')

    def _delete_default_text(self) -> None:
        """
        Delete the default text in the entry field.
        """
        if self._msg_entry.get() == 'Message':
            self._msg_entry.delete(0, END)
            self._msg_entry.config(foreground='black')

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def add_message(self, msg: str):
        pass

    @abstractmethod
    def set_participants_label(self, label: str):
        pass

    @abstractmethod
    def show_server_error(self):
        pass

    @abstractmethod
    def deiconify_parent_root(self):
        pass

    @abstractmethod
    def destroy(self):
        pass


class ClientChatWindow(ChatWindow):
    """
    Class for the client chat window.

    Attributes:
        socket (ClientSocket): The client socket object for communication with the server.

    Methods:
        connect():
            Connect to the server.
        _send_message():
            Send a message to other participants of the chat.
        add_message(msg: str):
            Display a message on the screen.
        set_participants_label(label: str):
            Update the label showing the number of participants.
        _open_list_of_participants():
            Open the window with a list of participants.
        show_server_error():
            Show a server error through a messagebox.
        deiconify_parent_root():
            Reopen the parent window.
        destroy():
            Destroy the client chat window.

    """
    def __init__(self, parent) -> None:
        """
        Initialize the chat window.

        Args:
            parent (MainWindow): Parent window.
        """
        super().__init__(parent)
        self.socket = ClientSocket(self)
        self._participants_label.bind('<Button-1>', lambda event: self._open_list_of_participants())

    def connect(self) -> None:
        """
        Connect to server.
        """
        self.socket.connect()

    def _send_message(self) -> None:
        """
        Send a message to other participants of chat.
        """
        if self._msg_entry.get() and self._msg_entry.get() != "Message":
            curr_time = datetime.now().time()
            time = curr_time.strftime('%H:%M')
            message = f'{self._master.user.name}: {self._msg_entry.get()}\n{time}\n\n'
            self.socket.send(message)
            self._msg_entry.delete(0, END)

    def add_message(self, msg: str) -> None:
        """
        Display message on the screen.

        Args:
            msg (str): New message to display on screen.
        """
        self._text_widget.config(state=NORMAL)
        self._text_widget.insert(END, msg)
        self._text_widget.see(END)
        self._text_widget.config(state=DISABLED)

    def set_participants_label(self, label: str) -> None:
        """
        Update the label showing a number of participants.

        Args:
            label (str): The new label to display.
        """
        self._num_of_participants.set(label)

    def _open_list_of_participants(self) -> None:
        """
        Open the window with list of participants.
        """
        participants_list = ttk.Toplevel(title='Participants')
        participants_list.iconbitmap('./rsrc/chat.ico')

        x_position = (self.root.winfo_screenwidth() - 350) // 2
        y_position = (self.root.winfo_screenheight() - 400) // 2

        participants_list.geometry(f'350x400+{x_position}+{y_position - 30}')
        participants_list.minsize(350, 400)

        my_list = tk.Listbox(participants_list, font=('Microsoft JhengHei Light', 10), foreground='black',
                             selectborderwidth=1)
        my_list.pack(padx=5, pady=5, fill='both', expand=True)

        for nick in self.socket.participants:
            my_list.insert(END, nick)

        participants_list.mainloop()

    def show_server_error(self) -> None:
        """
        Show a server error through messagebox.
        """
        messagebox.showerror(title='Error', message="Server doesn't answer. Please try again.")

    def deiconify_parent_root(self) -> None:
        """
        Reopen parent window.
        """
        self.socket.close()
        self._master.deiconify_main_window()

    def destroy(self) -> None:
        """
        Destroy client chat window.
        """
        self.root.destroy()
