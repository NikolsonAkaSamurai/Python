from tkinter import *

class my_gui(Tk):

    def __init__(self, width, height, title):

        text = ""
        text += str(width) + "x"
        text += str(height)
        super(my_gui).__init__()
        super(my_gui).title(title)
        super(my_gui).geometry(text)

    def my_main_loop(self):
        self.mainloop()