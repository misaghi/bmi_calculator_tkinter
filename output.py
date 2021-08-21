import tkinter as tk
import tkinter.ttk as ttk

from indicator import Indicator

class Output(ttk.Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)

        self.scale_var = tk.IntVar()
        self.arrow_image = tk.PhotoImage(file='assets/pictures/arrow.png')
        self.y_position = 691

        indicator = Indicator(self)

        self.canvas = tk.Canvas(self, background='white', width=60)
        self.arrow = self.canvas.create_image((50, self.y_position), image=self.arrow_image)
        self.bmi = self.canvas.create_text((19, self.y_position), text='0.0')

        self.canvas.pack(side=tk.LEFT, fill=tk.Y)
        indicator.pack(side=tk.LEFT)

    # Calculations here are more experimental than given by a formula but you can note that
    # every line is 8px. So with this we can formularize our calculations.
    @staticmethod
    def set_bmi(self, bmi):
        if bmi == 0:
            y_pointer = 679
        elif bmi < 18.5:
            y_pointer = 390 + (18.5 - bmi) * 16
        elif bmi < 25:
            y_pointer = 267 + (25 - bmi) * 16
            if bmi >= 21.75:
                y_pointer -= 10 # -10 This is for better accuracy.
        elif bmi < 30:
            y_pointer = 178 + (30 - bmi) * 16 - 10 # -10 This is for better accuracy.
        elif bmi < 35:
            y_pointer = 89 + (35 - bmi) * 16 - 10 # -10 This is for better accuracy.
        else:
            if bmi >= 40:
                y_pointer = -3 # Here it goes out of our scale.
            else:
                y_pointer = 9 + (40 - bmi) * 16 - 15 # -15 This is for better accuracy.
        y_num = y_pointer + 3

        self.canvas.itemconfig(self.bmi, text=bmi)
        self.canvas.moveto(self.arrow, y=y_pointer)
        self.canvas.moveto(self.bmi, y=y_num)