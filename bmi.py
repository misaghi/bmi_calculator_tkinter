import tkinter as tk
import tkinter.ttk as ttk

from output import Output
from input import Input
from popup import Popup

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('BMI Calculator')
        self.resizable(False, False)
        self.minsize(532, 700)

        out = Output(self)
        inp = Input(self, out)

        menu = tk.Menu(self)
        menu.add_command(label='About', command=self.show_about)

        self.config(menu=menu)

        inp.pack(side=tk.LEFT, anchor=tk.N, pady=60, padx=30)
        out.pack(side=tk.RIGHT)

    def show_about(self):
        about = Popup(self, mode='info', resizable=False, title='About', message='''A small project by
Seyed Amirhossein Misaghi
CE student University of Guilan
Summer 1400
        ''')

if __name__ == '__main__':
    app = App()
    app.mainloop()