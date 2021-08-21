import tkinter as tk
import tkinter.ttk as ttk

class Popup(tk.Toplevel):
    '''This is a simple class representing a custom toplevel(sth like a messagebox)
    Acceptable modes: 'error', 'info'
    '''

    def __init__(self, master=None, **kw):
        mode = kw.pop('mode')
        title = kw.pop('title')
        resizable = kw.pop('resizable')
        message = kw.pop('message')
        
        super().__init__(master=master, **kw)

        self.title(title)
        self.resizable(resizable, resizable)

        self.image_picker(mode)

        ttk.Label(
            self, text=message, image=self.image, compound=tk.LEFT, justify=tk.LEFT
        ).pack(padx=(0, 5))

    def image_picker(self, mode):
        if mode == 'error':
            self.image = tk.PhotoImage(file='assets/pictures/error.png')
        elif mode == 'info':
            self.image = tk.PhotoImage(file='assets/pictures/info.png')