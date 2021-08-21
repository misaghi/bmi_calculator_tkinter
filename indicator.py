import tkinter as tk
import tkinter.ttk as ttk

class Indicator(ttk.Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)

        tk.Label(
            self, text='EXTREMELY OBESE\n<35', background='#f95353', foreground='#ffffff', height=5
        ).pack(fill=tk.X, ipadx=4)
        tk.Label(
            self, text='OBESE\n30-34.9', background='#fd802e', foreground='#ffffff', height=5
        ).pack(fill=tk.X)
        tk.Label(
            self, text='OVERWEIGHT\n25-29.9', background='#eee133', foreground='#ffffff', height=5
        ).pack(fill=tk.X)
        tk.Label(
            self, text='NORMAL\n18.5-24.9', background='#3dd365', foreground='#ffffff', height=7
        ).pack(fill=tk.X)
        tk.Label(
            self, text='UNDERWEIGHT\n<18.5', background='#87b1d9', foreground='#ffffff', height=18
        ).pack(fill=tk.X)


if __name__ == '__main__':
    root = tk.Tk()
    e = Indicator(root)
    e.pack()
    e.mainloop()