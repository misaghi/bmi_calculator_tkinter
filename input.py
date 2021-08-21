import tkinter as tk
import tkinter.ttk as ttk

from entries import Entries
from arithmetic import Arithmetic
from popup import Popup

class Input(ttk.Frame):

    def __init__(self, master=None, out=None, **kw):
        super().__init__(master=master, **kw)

        self.output = out
        self.mode = 'SI' # Ues kg,m or lb,in

        self.entries = Entries(self, unit_h='m', unit_w='kg')
        self.change_units = ttk.Button(self, text='kg -> lb\nm -> in', command=self.kg_to_lb_m_to_in)

        self.entries.pack()
        ttk.Button(self, text='Calculate', command=self.calculate).pack(pady=(30, 10), fill=tk.X)
        self.change_units.pack(padx=30, pady=(10, 30), ipadx=5, ipady=5)

    def calculate(self):
        results = self.entries.get_values
        arithmetic = Arithmetic(results[2], results[3], self.mode)
        bmi = arithmetic.bmi
        if bmi is False:
            w = Popup(self, mode='error', resizable=False, title='Error', message='''Invalid inputs.
Height cannot be zero.
Weight cannot be zero.''')
        if results[0] == '' or results[1] == 0:
            w = Popup(self, mode='error', resizable=False, title='Error', message='''Invalid inputs. 
The name and age fields are required.''')
            self.entries.show_required()
        else:
            # I used a static method in output class and it needs a the current output.
            self.output.set_bmi(self.output, bmi)
            self.save_calculations(results[0], results[1], results[2], results[3], bmi)

    def kg_to_lb_m_to_in(self):
        self.change_units.config(text='lb -> kg\nin -> m', command=self.lb_to_kg_in_to_m)
        self.entries.update_unit_labels('in', 'lb')
        self.mode = 'US'

    def lb_to_kg_in_to_m(self):
        self.change_units.config(text='kg -> lb\nm -> in', command=self.kg_to_lb_m_to_in)
        self.entries.update_unit_labels('m', 'kg')
        self.mode = 'SI'

    # Here it write our inputs and calculations down in a simple text file
    def save_calculations(self, name, age, weight, height, bmi):
        with open('assets/data', 'a') as f:
            f.write('Name:{} Age:{} Weight:{} Height:{} BMI:{}\n'.format(name, age, weight, height, bmi))