import tkinter as tk
import tkinter.ttk as ttk

class Entries(ttk.Frame):

    NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.')

    def __init__(self, master=None, **kw):

        unit_h = kw.pop('unit_h')
        unit_w = kw.pop('unit_w')

        super().__init__(master=master, **kw)

        self.name_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()

        self.required = True

        yvcmd = (self.register(self.validate_if_number), '%P')

        self.name_entry = ttk.Entry(self, textvariable=self.name_var, width=25)
        self.age_entry = ttk.Entry(self, textvariable=self.age_var, validate='key', validatecommand=yvcmd, width=25, style='req.TEntry')
        self.weight_entry = ttk.Entry(self, textvariable=self.weight_var, validate='key', validatecommand=yvcmd, width=25)
        self.height_entry = ttk.Entry(self, textvariable=self.height_var, validate='key', validatecommand=yvcmd, width=25)

        self.height_unit_label = ttk.Label(self, text=unit_h)
        self.weight_unit_label = ttk.Label(self, text=unit_w)

        opts = {'sticky': tk.W, 'pady': 5, 'padx': (10, 0)}

        ttk.Label(self, text='Name:').grid(row=0, column=0, **opts)
        self.name_entry.grid(row=0, column=1, padx=10)
        
        ttk.Label(self, text='Age:').grid(row=1, column=0, **opts)
        self.age_entry.grid(row=1, column=1)
        
        ttk.Label(self, text='Weight:').grid(row=2, column=0, **opts)
        self.weight_entry.grid(row=2, column=1)
        self.weight_unit_label.grid(row=2, column=2, sticky=tk.W)
        
        ttk.Label(self, text='Height:').grid(row=3, column=0, **opts)
        self.height_entry.grid(row=3, column=1)
        self.height_unit_label.grid(row=3, column=2, sticky=tk.W)

    def validate_if_number(self, inp, mode=None):
        for i in inp:
            if i in self.NUMBERS:
                continue
            else:
                return False        
        return True

    def update_unit_labels(self, unit_h, unit_w):
        self.height_unit_label.config(text=unit_h)
        self.weight_unit_label.config(text=unit_w)

    @property
    def get_values(self):
        name = self.name_var.get()
        age = self.age_var.get()
        weight = self.weight_var.get()
        height = self.height_var.get()
        return name, age, weight, height